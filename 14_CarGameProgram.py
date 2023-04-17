command=""
started = False
stopped = False
while True:
    command=input(">").lower()
    if command == "start":
        if started:
            print("Car is already started")
        else:
            started=True
            print("Car Started...")
    elif command == "stop":
        if not stopped:
            print("Car is already stopped")
        else:
            started=False
            print("Car Stopped.")
    elif command =="help":
        print("""Start- To Start the Car
Stop-To Stop the Car
quit -To Quit the car""")
    elif command=='quit':
        break
    else:
        print("Sorry I canot understand that")
