def solution():
    """A shopkeeper bought 150 packets of milk. Each packet contained 250 ml of milk. If one fluid ounce is equal to 30 ml, how many ounces of milk did he buy?"""
    # Define the number of packets of milk and the volume of each packet
    packets = 150
    volume_per_packet = 250 # ml

    # Calculate the total volume of milk in milliliters
    total_volume = packets * volume_per_packet

    # Convert the total volume to fluid ounces
    fluid_ounce_conversion = 30 # ml
    total_volume_oz = total_volume / fluid_ounce_conversion

    # Display the total volume in fluid ounces
    result = total_volume_oz
    return result

print(solution())