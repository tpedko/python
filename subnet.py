#!/usr/bin/env python
# python subnet.py 200.100.33.65/26

import sys

# Get address string and CIDR string from command line
(addrString, cidrString) = sys.argv[1].split('/')

# Split address into octets and turn CIDR into int
addr = addrString.split('.')
cidr = int(cidrString)

# Initialize the netmask and calculate based on CIDR mask
mask = [0, 0, 0, 0]
for i in range(cidr):
	mask[int(i/8)] = mask[int(i/8)] + (1 << (7 - i % 8))

# Initialize net and binary and netmask with addr to get network
net = []
for i in range(4):
	net.append(int(addr[i]) & mask[i])

# Duplicate net into broad array, gather host bits, and generate broadcast
broad = list(net)
brange = 32 - cidr
for i in range(brange):
	broad[int(3 - i/8)] = broad[int(3 - i/8)] + (1 << (i % 8))

# Locate usable IPs
hosts = {"first":list(net), "last":list(broad)}
hosts["first"][3] += 1 # Normally +1 but AWS uses the first 4 IPs http://j.mp/2eeNF6f
hosts["last"][3] -= 1

# Count the difference between first and last host IPs
hosts["count"] = 0
for i in range(4):
    hosts["count"] += (hosts["last"][i] - hosts["first"][i]) * 2**(8*(3-i))

# Print information, mapping integer lists to strings for easy printing
if len(sys.argv) > 2:
    print ("")
    print ("Name:       ", sys.argv[2])
print ("CIDR:       ", addrString, "/", cidr)
print ("Address:    ", addrString)
print ("Netmask:    ", ".".join(map(str, mask)))
print ("Network:    ", ".".join(map(str, net)))
print ("Broadcast:  ", ".".join(map(str, broad)))
print ("Host Range: ", ".".join(map(str, hosts["first"])),"-",".".join(map(str, hosts["last"])))
print ("Host Count: ", hosts["count"])
