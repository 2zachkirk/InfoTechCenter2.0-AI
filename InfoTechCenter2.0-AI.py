import time
import sys

def welcome_message(delay=3):
    """Prints a welcome message and waits for a specified delay."""
    print("\n\nWelcome to InfoTech Center V1.0\n")
    time.sleep(delay)

def progress_bar(total_iterations=20, progress_char='.', progress_interval=0.5):
    """Displays a progress bar indicating the boot-up progress."""
    print("Boot Up Progress:")
    for i in range(1, total_iterations + 1):
        progress = progress_char * i
        sys.stdout.write("\r[{:<20}] {:>3}%".format(progress, int(i * 100 / total_iterations)))
        sys.stdout.flush()
        time.sleep(progress_interval)
    print("\nOperating System Booted Up - Retina Scanned - Access Granted!")

def main():
    welcome_message()
    try:
        progress_bar()
    except KeyboardInterrupt:
        print("\nBoot-up process interrupted by user.")
    except Exception as e:
        print("\nAn error occurred during boot-up:", e)

if __name__ == "__main__":
    main()


