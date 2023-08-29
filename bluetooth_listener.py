import bluetooth

print("Starting to scan for Bluetooth devices continuously...")

# Store previously found devices
known_devices = set()

while True:
    print("Looking for nearby devices...")
    nearby_devices = bluetooth.discover_devices(lookup_names=True, duration=8)

    # Print only the new devices
    for address, name in nearby_devices:
        if address not in known_devices:
            print(f"Found new device: {name} [{address}]")
            known_devices.add(address)

    print(f"Total devices found: {len(known_devices)}")

