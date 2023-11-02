def solution():
    # Define the number of packets and the amount of milk per packet
    num_packets = 150
    milk_per_packet = 250  # ml

    # Convert ml to fluid ounces
    ml_to_oz = 1/30  # 1 fluid ounce is equal to 30 ml
    milk_per_packet_oz = milk_per_packet * ml_to_oz

    # Calculate the total amount of milk in ounces
    total_milk_oz = num_packets * milk_per_packet_oz
    result = total_milk_oz
    return result

print(solution())