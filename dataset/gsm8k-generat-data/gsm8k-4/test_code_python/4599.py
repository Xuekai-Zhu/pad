def solution():
    """A shopkeeper bought 150 packets of milk. Each packet contained 250 ml of milk. If one fluid ounce is equal to 30 ml, how many ounces of milk did he buy?"""
    # Define the number of packets and the volume of milk in each packet
    packets = 150
    volume_per_packet = 250

    # Calculate the total volume of milk in ml
    total_volume_ml = packets * volume_per_packet

    # Convert ml to fluid ounces
    total_volume_oz = total_volume_ml / 30

    # return the result
    result = total_volume_oz
    return result

print(solution())