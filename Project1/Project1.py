def calculate_subnet_info(ip_subnet):
    ip_parts, subnet_mask = ip_subnet.split('/') #split into IP address and subnet mask
    ip_parts = ip_parts.split('.') #split IP into 4 components

    # Convert IP address to binary
    ip_binary = ''.join(format(int(part), '08b') for part in ip_parts)

    # Calculate the subnet address
    subnet_binary = ip_binary[:int(subnet_mask)] + '0' * (32 - int(subnet_mask)) #Use subnet mask to only keep the newtork portion of the IP address and turn host part to all 0s
    subnet_parts = [subnet_binary[i:i+8] for i in range(0, 32, 8)] #Take the string above and split into 4 8-bit binary strings stored in a list
    subnet_address = '.'.join(str(int(part, 2)) for part in subnet_parts) #Convert back to decimal form and separate by periods

    # Calculate the broadcast address
    broadcast_binary = ip_binary[:int(subnet_mask)] + '1' * (32 - int(subnet_mask)) #Use subnet mask to keep network portion and replace host portion with all 1's
    broadcast_parts = [broadcast_binary[i:i+8] for i in range(0, 32, 8)] #Divide Broadcase Address String into 4 8-bit parts
    broadcast_address = '.'.join(str(int(part, 2)) for part in broadcast_parts) #Convert back to strings and decimal form, seprarate by periods 

    # Calculate the valid host range
    network_bits = ip_binary[:int(subnet_mask)] #slice the network portion of IP
    first_host_binary = network_bits + '0' * (32 - int(subnet_mask) - 1) + '1' #add 1 to network address
    last_host_binary = network_bits + '1' * (32 - int(subnet_mask) - 1) + '0' #subtract 1 from broadcast address

    first_host_parts = [first_host_binary[i:i+8] for i in range(0, 32, 8)] #split into 4 substrings of 8 bits
    last_host_parts = [last_host_binary[i:i+8] for i in range(0, 32, 8)] #split into 4 substrings of 8 bits

    first_host_address = '.'.join(str(int(part, 2)) for part in first_host_parts) #join parts by periods and convert to decimal base 2 form
    last_host_address = '.'.join(str(int(part, 2)) for part in last_host_parts) #join parts by periods and convert to decimal base 2 form

    return subnet_address, broadcast_address, first_host_address, last_host_address


# User input
ip_subnet = input("Enter the IP address and subnet mask in CIDR notation (e.g., 123.43.2.1/24): ")

# Calculate subnet address, broadcast address, and valid host range
subnet_address, broadcast_address, first_host_address, last_host_address = calculate_subnet_info(ip_subnet)

# Print the results
print("Subnet Address:", subnet_address)
print("Broadcast Address:", broadcast_address)
print("Valid Host Range:", first_host_address, "-", last_host_address)
