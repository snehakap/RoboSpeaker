import os

if __name__ == '__main__':
    print("Welcome to RoboSpeaker")
    while True:
        x = input("Enter what you want me to say: ")
        if x == 'q' or 'Q':
            os.system("say 'Bye' ")
            break
        command = f"say {x}"
        os.system(command)
