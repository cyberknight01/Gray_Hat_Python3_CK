import my_debugger

debugger = my_debugger.debugger()
pid = input("Enter the PID of the process to attach to: ")
# 由于 input 函数的性质，将输入的字符转换为数字型
debugger.attach(int(pid))

list = debugger.enumerate_threads()

# 对于列表中的每个线程，我们试图提取出相应的上下文信息
for thread in list:
    thread_context = debugger.get_thread_context(thread)

    # 输出一些寄存器信息，%08x就是8位的十六进制，不够0补充
    print("[*] Dumping Registers for thread ID:0x%08x" % thread)
    print("[**] EIP:0x%08x" % thread_context.Eip)
    print("[**] ESP:0x%08x" % thread_context.Esp)
    print("[**] EBP:0x%08x" % thread_context.Ebp)
    print("[**] EAX:0x%08x" % thread_context.Eax)
    print("[**] EBX:0x%08x" % thread_context.Ebx)
    print("[**] ECX:0x%08x" % thread_context.Ecx)
    print("[**] EDX:0x%08x" % thread_context.Edx)
    print("[*] END DUMP")
debugger.detach()