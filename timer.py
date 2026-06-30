import time
import sys
import os

def clear_screen():
    """Clears the terminal screen."""
    os.system('cls' if os.name == 'nt' else 'clear')

def countdown(total_seconds, label="Time"):
    """A simple countdown timer that updates in the terminal."""
    while total_seconds > 0:
        mins, secs = divmod(total_seconds, 60)
        time_format = f"{mins:02d}:{secs:02d}"
        
        # Now it uses the custom label
        sys.stdout.write(f"\r{label} Remaining: {time_format}")
        sys.stdout.flush()
        
        time.sleep(1)
        total_seconds -= 1
        
    print(f"\n{label} complete!")

if __name__ == "__main__":
    # Set standard Pomodoro focus time (25 minutes = 1500 seconds)
    POMODORO_SECONDS = 1500
    countdown(POMODORO_SECONDS)
