from netmiko import ConnectHandler

ip_range = 0
iplist = ["192.168.26.10", "192.168.26.20"]

for ip_addr in iplist:
    ip_range = ip_range + 1
    # Set the device information and credentials
    device = {
        "device_type": "cisco_ios",
        "ip": ip_addr,
        "username": "cisco",
        "password": "cisco",
    }

    # Connect to the device
    net_connect = ConnectHandler(**device)
    
    # Create a list of commands to configure loopback interface
    commands = [
        "interface loopback "+str(ip_range),
        "ip address 172.16."+str(ip_range)+".1"
        " 255.255.255.0",
        "end",
        "write memory",
    ]
    
    # Send the commands to the device
    output = net_connect.send_config_set(commands)
    
    #print(output)

    # Close the connection
    net_connect.disconnect()
    
