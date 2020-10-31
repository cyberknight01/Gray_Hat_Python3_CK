import my_debugger

debugger = my_debugger.debugger()
pid = input("请输入待调试进程的进程号:")
# 由于 input 函数的性质，将输入的字符转换为数字型
debugger.attach(int(pid))
debugger.detach()
