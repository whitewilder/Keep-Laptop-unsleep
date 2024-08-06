import ctypes
import time
import win32api, win32con
now=time.time()
def click(x,y):
  win32api.SetCursorPos((x,y))
  win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,x,y,0,0)
  win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,x,y,0,0)
def move_cursor(x,y):
  win32api.SetCursorPos((x,y))

while True:
  if n-now()>30:
    ctypes.windll.kernal32.SetThreadExecutionState(0x80000002)
    click(10,10)
    click(10,11)
    move_cursor(20,10)
    now=time.time()
    time.sleep(330)
  
