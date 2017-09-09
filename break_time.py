import time
import webbrowser

print("This program started on"+time.ctime())
for x in range(1,3):
    time.sleep(2*60*60)
    webbrowser.open("https://www.youtube.com/watch?v=56bSAWFgZ1I")
