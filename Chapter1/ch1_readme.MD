### python3中由于使用的是Unicode编码，而ctype中的printf无法使用；所以需要编码处理
###有三种方式

#### 转为byte类型 在字符串前面加b
###### message_string = b"Hello world!\n"

#### 使用wprintf宽字符显示
###### msvcrt.wprintf("Testing:%s",message_string)

### 转码为utf-8
###### message_string = "Hello world!\n"
###### result = message_string.encode("utf-8")
###### msvcrt.printf(result)

