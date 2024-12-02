import os
import time

def main():
    print("\033[92m")  # Set terminal color to green
    print("Hello, do you love me? (Answer in only yes/no)")
    user_input = input("Your answer: ").strip().lower()

    if user_input == "yes":
        love()
    elif user_input == "no":
        hate()
    else:
        print("Invalid input. Please answer with yes or no.")
        main()  # Restart the process if the input is invalid

def love():
    print("I Love You Too... ❤️❤️❤️")
    print("See You Later")
    input("Press Enter to exit...")

def hate():
    print("But I Love You Too... 😢😢😢")
    print("Bleh, you deserve it!")
    time.sleep(3)
    put_system_to_sleep()

def put_system_to_sleep():
    if os.name == "nt":  # Check if the OS is Windows
        os.system("rundll32.exe powrprof.dll,SetSuspendState 0,1,0")  # Windows sleep command
    else:
        print("Sleep mode is not supported on this operating system.")
        input("Press Enter to exit...")

if __name__ == "__main__":
    main()
