import time

def time_convert(sec):
    mins = sec // 60
    sec = sec % 60 
    hours = sec // 60
    mins = mins % 60
    
    print("TIme Lapsed = {0}:{1}:{2}".format(int(hours),int(mins),int(sec)))
    
input("Press Enter to Start")
start_time = time.time()

input("press Enter to Stop")
end_time = time.time()

time_lapsed = end_time - start_time
time_convert(time_lapsed)