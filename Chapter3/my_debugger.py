from ctypes import *
from my_debugger_defines import *

kernel32 = windll.kernel32

class debugger():
    def __int__(self):
        pass

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

        else:
            print("[*] Error:0x%08x." % kernel32.GetLastError())

