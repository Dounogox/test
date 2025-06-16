import time 

def chaohoi():
    hour = time.localtime().tm_hour
    if hour < 12:
        print("\nChào buổi sáng!")
    elif hour < 18:
        print("\nChào buổi chiều!")
    else:
        print("\nChào buổi tối!")