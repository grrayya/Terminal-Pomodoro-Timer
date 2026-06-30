import time
import sys
import os

def clear_screen():
    """Clears the terminal screen."""
    os.system('cls' if os.name == 'nt' else 'clear')

def countdown(total_seconds):
    """A simple countdown timer that updates in the terminal."""
    while total_seconds > 0:
        # Calculate minutes and seconds
        mins, secs = divmod(total_seconds, 60)
        
        # Format the time as MM:SS
        time_format = f"{mins:02d}:{secs:02d}"
        
        # Print the time, using \r to overwrite the current line
        sys.stdout.write(f"\rFocus Time Remaining: {time_format}")
        sys.stdout.flush()
        
        # Wait one second and reduce the total time
        time.sleep(1)
        total_seconds -= 1
        
    print("\nTime's up! Great job.")

if __name__ == "__main__":
    # Set standard Pomodoro focus time (25 minutes = 1500 seconds)
    POMODORO_SECONDS = 1500
    countdown(POMODORO_SECONDS)
