time = input("Enter time in seconds: ")
time = int(time)
hours = time // 3600
minutes = (time % 3600) // 60
seconds = time % 60
print("%02d:%02d:%02d" % (hours, minutes, seconds))
