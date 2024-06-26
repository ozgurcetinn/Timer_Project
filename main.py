import time
import sys

def countdown_timer(seconds):
    try:
        while seconds:
            mins, secs = divmod(seconds, 60)
            timer = '{:02d}:{:02d}'.format(mins, secs)
            print(timer, end="\r")
            time.sleep(1)
            seconds -= 1
            print(seconds)
        print("Time's up!")
    except KeyboardInterrupt:
        print("\nTimer stopped by user.")
        sys.exit()

if __name__ == "__main__":
    try:
        seconds = int(input("Enter the time in seconds: "))
        countdown_timer(seconds)
    except ValueError:
        print("Please enter a valid number.")

