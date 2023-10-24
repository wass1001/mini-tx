import subprocess
import re

# Run the netsh command to get the profile names
output = subprocess.run(['netsh', 'wlan', 'show', 'profiles'], capture_output=True).stdout.decode()

# Use regex to get the profile names
profile_names = (re.findall('All User Profile     : (.*)\r', output))

# Create a dictionary to store the profiles and passwords
wifi_profiles = {}

# Loop through the profile names
for name in profile_names:
    # Run the netsh command to get the password for the profile
    profile_info = subprocess.run(['netsh', 'wlan', 'show', 'profile', name, 'key=clear'],
                                  capture_output=True).stdout.decode()

    # Use regex to get the password
    password = re.findall('Key Content            : (.*)\r', profile_info)

    # Add the profile and password to the dictionary
    wifi_profiles[name] = password

# Print the profiles and passwords
for name, password in wifi_profiles.items():
    print(f'WiFi Network: {name}, Password: {password}')
