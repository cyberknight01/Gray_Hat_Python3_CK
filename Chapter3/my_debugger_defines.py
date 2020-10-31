from ctypes import *

# 为 ctype 变量创建符合匈牙利风命名风格的命名，这样可以使代码更接近 Win32 的风格
WORD = c_ushort
DWORD = c_ulong
LPBYTE = POINTER(c_ubyte)
LPTSTR = POINTER(c_char)
HANDLE = c_void_p

# 定义常值
DEBUG_PROCESS = 0x00000001
CREATE_NEW_CONSLOE = 0x00000010

# 定义函数 CreateProcessA()/CreateProcessW() 所需要的结构体
class STARTUPINFO(Structure):
    _fieles_ =[
        ("cb",              DWORD),
        ("lpReserved",      LPTSTR),
        ("lpDesktop",       LPTSTR),
        ("lpTitle",         LPTSTR),
        ("dwX",             DWORD),
        ("dwY",             DWORD),
        ("dwXSize",         DWORD),
        ("dwYSize",         DWORD),
        ("dwXCountChars",   DWORD),
        ("dwYCountChars",   DWORD),
        ("dwFillAttribute", DWORD),
        ("dwFlags",         DWORD),
        ("wShowWindow",     WORD),
        ("cbReserved2",     WORD),
        ("lpReserved2",     LPBYTE),
        ("hStdInput",       HANDLE),
        ("hStdOutput",      HANDLE),
        ("hStdError",       HANDLE),
    ]

class PROCESS_INFORMATION(Structure):
    _fields_ = [
        ("hProcess",        HANDLE),
        ("hThread",         HANDLE),
        ("dwProcessId",     DWORD),
        ("dwThreadId",      DWORD),
    ]

