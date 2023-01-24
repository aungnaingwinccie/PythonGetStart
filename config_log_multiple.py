from netmiko import ConnectHandler
ip_addr = ["192.168.6.12", "192.168.6.13"]
for iplist in ip_addr:
       
    # Set the device information and credentials
    device = {
        "device_type": "cisco_ios",
        "ip": iplist,
        "username": "cisco",
        "password": "cisco",
    }

    # Connect to the device
    net_connect = ConnectHandler(**device)

    # Execute the "show running-config" command and store the output
    output = net_connect.send_command("show running-config")

    # Write the output to a file
    with open("running_config_" + iplist + ".txt", "w") as file:
        file.write(output)

    # Close the connection
    net_connect.disconnect()
