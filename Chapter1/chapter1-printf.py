from ctypes import *
msvcrt = cdll.msvcrt
#message_string = b"Hello world!\n"
#msvcrt.printf(b"Testing:%s",message_string)
message_string = "Hello world!\n"
result = message_string.encode("utf-8")
msvcrt.printf(b"Testing:%s",result)
