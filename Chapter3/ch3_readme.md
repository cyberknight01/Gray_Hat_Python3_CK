## 本章使用的关键函数  
#### 3.1 本节使用相关函数及结构体
##### 创建新进程，新进程在调用进程的安全上下文中运行
```cython
BOOL WINAPI CreateProcessW(
  LPCWSTR               lpApplicationName,
  LPWSTR                lpCommandLine,
  LPSECURITY_ATTRIBUTES lpProcessAttributes,
  LPSECURITY_ATTRIBUTES lpThreadAttributes,
  BOOL                  bInheritHandles,
  DWORD                 dwCreationFlags,
  LPVOID                lpEnvironment,
  LPCWSTR               lpCurrentDirectory,
  LPSTARTUPINFOW        lpStartupInfo,
  LPPROCESS_INFORMATION lpProcessInformation
);
```

##### 指定在创建进程时的窗口，桌面，句柄和主窗口的外观
```cython
typedef struct _STARTUPINFOW {
  DWORD  cb;
  LPWSTR lpReserved;
  LPWSTR lpDesktop;
  LPWSTR lpTitle;
  DWORD  dwX;
  DWORD  dwY;
  DWORD  dwXSize;
  DWORD  dwYSize;
  DWORD  dwXCountChars;
  DWORD  dwYCountChars;
  DWORD  dwFillAttribute;
  DWORD  dwFlags;
  WORD   wShowWindow;
  WORD   cbReserved2;
  LPBYTE lpReserved2;
  HANDLE hStdInput;
  HANDLE hStdOutput;
  HANDLE hStdError;
} STARTUPINFOW, *LPSTARTUPINFOW;
```
##### 包含新创建的进程及其主线程的有关信息,它常与 CreateProcess，CreateProcessAsUser，CreateProcessWithLogonW或CreateProcessWithTokenW函数一起使用
```cython
typedef struct _PROCESS_INFORMATION {
  HANDLE hProcess;
  HANDLE hThread;
  DWORD  dwProcessId;
  DWORD  dwThreadId;
} PROCESS_INFORMATION, *PPROCESS_INFORMATION, *LPPROCESS_INFORMATION;
```

##### 动态链接库kernel32.dll导出函数OpenProcess(），获取进程的句柄
```python
HANDLE WINAPI OpenProcess(
    DWORD dwDesiredAccess,    //便是向目标进程索取哪种类型的访问权限
    BOOL  bInheritHandle,
    DWORD dwProcessId
);

```

##### 实现进程的附加函数
```python
BOOL WINAPI DebugActiveProcess(
  DWORD dwProcessId         //被附加的目标进程ID
);

```

##### 等待正在调试的进程中发生调试事件
```python
BOOL WINAPI WaitForDebugEvent(
  LPDEBUG_EVENT lpDebugEvent,
  DWORD         dwMilliseconds
);
```
##### 使调试器可以继续先前报告调试事件的线程
```python
BOOL WINAPI ContinueDebugEvent(
  DWORD dwProcessId,
  DWORD dwThreadId,
  DWORD dwContinueStatus
);
```

##### 停止调试器调试指定的进程
```python
BOOL WINAPI DebugActiveProcessStop(
  DWORD dwProcessId                 //停止调试的进程的标识符
);
如果函数成功，则返回值为非零
如果函数失败，则返回值为零
```

#### 3.2 获取寄存器状态信息
##### 获取线程的句柄函数
```cython
HANDLE WINAPI OpenThread(
  DWORD dwDesiredAccess,            //对线程对象的访问权限。线程的安全描述符检查此访问权限，此参数可以是一个或多个线程访问权限
  BOOL  bInheritHandle,             //如果该值为TRUE，则此进程创建的进程将继承该句柄。否则，进程将不会继承此句柄
  DWORD dwThreadId                  //要打开的线程的标识符
);
如果函数成功，则返回值是指定线程的打开句柄
如果函数失败，则返回值为NULL
```

##### 线程枚举，拍摄指定进程以及这些进程使用的堆，模块和线程的快照
```cython
HANDLE WINAPI CreateToolhelp32Snapshot(
  DWORD dwFlags,                    //快照中要包括的系统信息部分，是线程列表，进程列表，模块列表还是堆列表，具体可查MSDN
  DWORD th32ProcessID               //要包含在快照中的进程的进程标识符。此参数可以为零以指示当前进程，具体可查MSDN
);
```
##### 检索有关系统快照中遇到的任何进程的第一个线程的信息
```cython
BOOL WINAPI Thread32First(
  HANDLE          hSnapshot,        //从上一次调用CreateToolhelp32Snapshot函数返回的快照的 句柄
  LPTHREADENTRY32 lpte              //指向THREADENTRY32结构的指针
);
```

##### 检索有关系统内存快照中遇到的任何进程的下一个线程的信息
```cython
BOOL WINAPI Thread32Next(
  HANDLE          hSnapshot,
  LPTHREADENTRY32 lpte
);
```

##### 这个结构体包含枚举到的首个线程的相关信息
```cython
typedef struct tagTHREADENTRY32 {
  DWORD dwSize;                     //结构的大小，以字节为单位
  DWORD cntUsage;                   //该成员不再使用，并且始终设置为零
  DWORD th32ThreadID;               //线程标识符，与CreateProcess函数返回的线程标识符兼容
  DWORD th32OwnerProcessID;         //创建线程的进程的标识符
  LONG  tpBasePri;                  //分配给线程的内核基本优先级。优先级是从0到31的数字，0表示最低的线程优先级
  LONG  tpDeltaPri;                 //该成员不再使用，并且始终设置为零
  DWORD dwFlags;                    //该成员不再使用，并且始终设置为零
} THREADENTRY32;
```







在Python3中是没有raw_input()函数的，只有input()函数，input()无论输入数字和文本，输出都是文本，  
在Python3中，使用数字的时候就需要自己来进行转换了，在让用户输入数字的时候一定切忌要进行转换，如果我们要使用数字的化。  

在Windows10中，打开计算器需要计算器显示在桌面或前台，当进入到后台或放到任务栏，通过进程查看是挂起状态，会导致试失败  


