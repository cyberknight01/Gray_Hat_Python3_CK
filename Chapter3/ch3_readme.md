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