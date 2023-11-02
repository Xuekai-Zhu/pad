def solution():
    # Find out how many plants were grown from each seed packet
    plants_per_packet = 9 / 3  # 3 seed packets grew 9 plants, so each seed packet grew 3 plants

    # Find out how many more plants Carter needs
    plants_needed = 12 - 9  # Carter wants a total of 12 plants, but he already grew 9

    # Find out how many more seed packets he needs to grow the remaining plants
    packets_needed = plants_needed / plants_per_packet

    result = packets_needed
    return result

print(solution())