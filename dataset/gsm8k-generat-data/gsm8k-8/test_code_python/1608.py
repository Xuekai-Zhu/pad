def solution():
    # Calculate the number of plants per seed packet
    plants_per_packet = 9 / 3

    # Calculate the number of additional packets needed to reach 12 plants
    additional_packets = (12 - 9) / plants_per_packet

    result = additional_packets
    return result

print(solution())