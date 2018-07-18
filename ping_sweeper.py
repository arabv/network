#ping inserted range of hosts

import subprocess   #module for cmd command "ping"

network_start=input("Insert your starting address\n")
print("Your starting address ", network_start)
network_end=input("Insert your end address\n")
print("Your last address is ", network_end,'\n')

start=network_start.split(".",3)
end=network_end.split(".",3)

network_prefix='.'.join(start[:3])

start=int(start[3])
end=int(end[3])+1

for i in range (start, end):
    network=network_prefix + '.' + str(i)
    subprocess.run(["ping", "-c", '1', "-W", '5', network])
