from ctypes import *
from my_debugger_defines import *

kernel32 = windll.kernel32

class debugger():
    def __int__(self):
        self.h_process = None
        self.pid = None
        self.debugger_active = None

    def load(self,path_to_exe):
        # 参数 dwCreationFlags 中的标志位控制着进程的创建方式，你若希望
        # 新创建的进程独占一个新的控制台窗口，而不是与父进程共用
        # 同一个控制台，可以加上标志位 CREATE_NEW_CONSLOE 
        creation_flags = DEBUG_PROCESS

        # 实例化之前定义的结构体
        startupinfo = STARTUPINFO()
        process_information = PROCESS_INFORMATION()

        # 在以下两个成员变量的共同作用下，新建进程将在一个单独的窗体中
        # 被显示，你可以通过改变结构体 STARTUPINFO 中的各成员
        # 变量的值来控制 debugger 进程的行为
        startupinfo.dwFlags = 0x1
        startupinfo.wShowWindow = 0x0

        # 设置结构体 STARTUPINFO 中的成员变量 cb 的值，
        # 用来表示结构体本身的大小
        startupinfo.cb = sizeof(startupinfo)

        # 此处由于CreateProcessA()传递的参数需要ASCII编码，而python3默认UNICODE编码
        # 所以使用CreateProcessW()
        if kernel32.CreateProcessW(path_to_exe,
                                   None,
                                   None,
                                   None,
                                   None,
                                   creation_flags,
                                   None,
                                   None,
                                   byref(startupinfo),
                                   byref(process_information)):
            print("[*] We have sucessfully launched the process!")
            print("[*] PID:%d" % process_information.dwProcessId)

            # 保存一个指向新建进程的有效句柄，以供
            # 后续的进程访问所使用
            self.h_process = self.open_process(process_information.dwProcessId)

        else:
            print("[*] Error:0x%08x." % kernel32.GetLastError())

    def open_process(self,pid):
        h_process = kernel32.OpenProcess(PROCESS_ALL_ACCESS,False,pid)
        return h_process

    def attach(self,pid):
        self.h_process = self.open_process(pid)

        # 试图附加到目标进程，若附加操作失败，则在输出提示信息后返回
        if kernel32.DebugActiveProcess(pid):
            self.debugger_active = True
            self.pid = int(pid)
            self.run()
        else:
            print("[*] Unable to attach to the process.")

    def run(self):
        # 现在我们等待发生在debugger进程中的调试事件
        while self.debugger_active == True:
            self.get_debug_event()

    def get_debug_event(self):
        debug_event = DEBUG_EVENT()
        continue_status = DBG_CONTINUE

        if kernel32.WaitForDebugEvent(byref(debug_event),INFINITE):
            # 目前我们还没有构建任何与事件处理相关的功能逻辑
            # 这里我们只是简单的恢复执行目标进程
            input("press a key to continue...")
            self.debugger_active = False
            kernel32.ContinueDebugEvent(
                debug_event.dwProcessId,
                debug_event.dwThreadId,
                continue_status
            )

    def detach(self):
        if kernel32.DebugActiveProcessStop(self.pid):
            print("[*] Finished debugging. Exiting...")
            return True
        else:
            print("There was an error")
            return False