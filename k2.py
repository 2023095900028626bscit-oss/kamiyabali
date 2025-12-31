from datetime import datetime
import time

while True:
    now = datetime.now()
    
    date = now.strftime("%A, %d %B %Y")
    current_time = now.strftime("%H:%M:%S")
    
    print(f"Date: {date}")
    print(f"Time: {current_time}")
    print("-" * 30)
    
    time.sleep(1)
