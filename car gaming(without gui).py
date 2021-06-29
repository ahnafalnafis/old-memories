def car_gaming():
    print("Welcome to Car Gaming!\nType help to get instructions-")
    command = ""
    started = False

    instructions = '''Type "start" - to start the car.
Type "stop" - to stop the car.
Type "exit" - to exit from the game.'''

    while True:
        command = input(">> ").lower()
        if command == "start":
            if started:
                print("Hey! Car is already started.")
            else:
                started = True
                print("Car is started...")
        elif command == "stop":
            if not started:
                print("Hey! car is already stopped.")
            else:
                started = False
                print("Car is stopped.")
        elif command == "help":
            print(instructions)
        elif command == "exit":
            press = ""
            while True:
                press = input("Thanks for playing.\nPress enter key to exit: ")
                if press == "":
                    exit()
                else:
                    print("Sorry! try again.")
        else:
            print("Sorry! I don't understand your command.")


car_gaming()
