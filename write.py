address = ["192.168.1.1", "172.16.1.1", "10.1.1.1"]
for ip_data in address:
    ipaddr = open("ip_address.txt", "a")
    ipaddr.write(str(ip_data)+"\n")
    ipaddr.close()