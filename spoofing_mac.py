import subprocess
import sys

interface = sys.argv[1]
new_mac = sys.argv[2]

# Disable the interface
subprocess.call(["ifconfig", interface, "down"])

# Set the new MAC address
subprocess.call(["ifconfig", interface, "hw", "ether", new_mac])

# Re-enable the interface
subprocess.call(["ifconfig", interface, "up"])

# Verify the change
result = subprocess.check_output(["ifconfig", interface])
if new_mac in result:
    print("[+] MAC address successfully changed to " + new_mac)
else:
    print("[-] MAC address change failed")

    #note this is only for Linux systems
    
    
    import subprocess

interface = "en0"
new_mac = "00:11:22:33:44:55"

subprocess.call(["sudo", "ifconfig", interface, "down"])
subprocess.call(["sudo", "ifconfig", interface, "ether", new_mac])
subprocess.call(["sudo", "ifconfig", interface, "up"])

#for mac os

