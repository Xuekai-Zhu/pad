def solution():
    num_plants = 9
    num_seed_packets = 3
    target_num_plants = 12

    # Calculate how many more plants Carter needs
    remaining_plants = target_num_plants - num_plants

    # Calculate how many more seed packets Carter needs, assuming each packet yields 3 plants
    remaining_seed_packets = remaining_plants // 3 + (remaining_plants % 3 > 0)

    result = remaining_seed_packets
    return result

print(solution())