#Taking log or configuration from Router or Switch.

from netmiko import ConnectHandler

# Set the device information and credentials
device = {
    "device_type": "cisco_ios",
    "ip": "192.168.6.12",
    "username": "cisco",
    "password": "cisco",
}

# Connecting to the device
net_connect = ConnectHandler(**device)

# Execute the "show running-config" command and store the output
output = net_connect.send_command("show running-config")

# Write the output to a file
# Using "with" no need to close the file back

with open("running_config.txt", "w") as file:
    file.write(output)

# Close the connection
net_connect.disconnect()