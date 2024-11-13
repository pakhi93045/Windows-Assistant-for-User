import time
import datetime
import ctypes
import sys
import os

# Function to handle focus mode logic
def focus_mode(Stop_time):
    current_time = datetime.datetime.now().strftime("%H:%M")
    a = current_time.replace(":", ".")
    a = float(a)
    b = Stop_time.replace(":", ".")
    b = float(b)
    Focus_Time = b - a
    Focus_Time = round(Focus_Time, 3)

    # Correct host path
    host_path = r'C:\Windows\System32\drivers\etc\hosts'
    redirect = '127.0.0.1'
    website_list = ["www.facebook.com", "facebook.com"]  # Websites to block

    print(f"Current time: {current_time}")
    print(f"Focus time: {Focus_Time}")
    time.sleep(2)

    if a < b:  # Only proceed if the stop time is greater than the current time
        try:
            with open(host_path, "r+") as file:  # Open the hosts file
                content = file.read()  # Read the existing content
                print(content)
                time.sleep(2)
                for website in website_list:
                    if website in content:
                        print(f"{website} is already blocked.")
                    else:
                        file.write(f"{redirect} {website}\n")  # Write the blocking rules
                        print(f"Blocking {website}")
                        time.sleep(1)

            print("FOCUS MODE TURNED ON !!!!")

            # Check for unblocking at the specified time
            while True:
                current_time = datetime.datetime.now().strftime("%H:%M")
                if current_time >= Stop_time:
                    with open(host_path, "r+") as file:
                        content = file.readlines()
                        file.seek(0)

                        for line in content:
                            if not any(website in line for website in website_list):
                                file.write(line)

                        file.truncate()
                        print("Websites are unblocked !!")

                    # Log the focus time
                    with open("focus.txt", "a") as file:
                        file.write(f",{Focus_Time}")  # Log the focus duration
                    break
        except PermissionError:
            print("Permission error: Cannot modify the hosts file.")
        except Exception as e:
            print(f"An error occurred: {e}")
    else:
        print("Stop time should be greater than current time.")

# Check for admin rights
def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False

# Ask for time input before elevating privileges
def get_user_input():
    Stop_time = input("Enter time to block websites (example: 10:10): ")  # Prompt for block time
    return Stop_time

# Main logic
if __name__ == "__main__":
    if is_admin():
        # If already an admin, call the focus mode with the input provided
        focus_mode(sys.argv[1])  # Pass the time argument
    else:
        # Get user input before elevating privileges
        Stop_time = get_user_input()

        # Re-run the script with admin rights, passing the Stop_time as an argument
        ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, f'{sys.argv[0]} {Stop_time}', None, 1)
