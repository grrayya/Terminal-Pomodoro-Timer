import time
import sys
import os
import datetime

def clear_screen():
    """Clears the terminal screen."""
    os.system('cls' if os.name == 'nt' else 'clear')

def log_session():
    """Saves a record of a completed focus session to a text file."""
    now = datetime.datetime.now()
    timestamp = now.strftime("%Y-%m-%d %H:%M:%S")
    
    with open("session_history.txt", "a") as file:
        file.write(f"Completed 25-minute focus session at: {timestamp}\n")

def countdown(total_seconds, label="Time"):
    """A simple countdown timer that updates in the terminal."""
    while total_seconds > 0:
        mins, secs = divmod(total_seconds, 60)
        time_format = f"{mins:02d}:{secs:02d}"
        
        sys.stdout.write(f"\r{label} Remaining: {time_format}")
        sys.stdout.flush()
        
        time.sleep(1)
        total_seconds -= 1
        
    print(f"\n{label} complete!\a")

if __name__ == "__main__":
    POMODORO_SECONDS = 1500  # 25 minutes
    BREAK_SECONDS = 300      # 5 minutes
    
    try:
        clear_screen()
        print("=== TERMINAL POMODORO ===")
        countdown(POMODORO_SECONDS, label="Focus Time")
        
        log_session()
        
        print("\nStarting break in 3 seconds...")
        time.sleep(3)
        
        clear_screen()
        countdown(BREAK_SECONDS, label="Break Time")
    except KeyboardInterrupt:
        print("\n\nTimer stopped. See you next time!")
