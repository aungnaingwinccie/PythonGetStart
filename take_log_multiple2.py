from netmiko import ConnectHandler

iplist = []

# Read IP addresses from existing text file ip_address.txt
ipaddr = open("ip_address.txt", "r")
IP = ipaddr.read()
iplist = IP.split("\n")
ipaddr.close()

for ip_addr in iplist:
       
    # Set the device information and credentials
    device = {
        "device_type": "cisco_ios",
        "ip": ip_addr,
        "username": "cisco",
        "password": "cisco",
    }
    print("Connecting to the device " + ip_addr + "...")
    # Connect to the device
    net_connect = ConnectHandler(**device)

    # Execute the "show running-config" command and store the output
    output = net_connect.send_command("show ip interface brief")

    # Write the output to a file
    with open("stack_status" + ip_addr + ".txt", "w") as file:
        file.write(output)

    # Close the connection
    net_connect.disconnect()