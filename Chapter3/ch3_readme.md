### 本章使用的关键函数
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
  DWORD dwProcessId
);
```

在Python3中是没有raw_input()函数的，只有input()函数，input()无论输入数字和文本，输出都是文本，  
在Python3中，使用数字的时候就需要自己来进行转换了，在让用户输入数字的时候一定切忌要进行转换，如果我们要使用数字的化。  

在Windows10中，打开计算器需要计算器显示在桌面或前台，当进入到后台或放到任务栏，通过进程查看是挂起状态，会导致试失败  


