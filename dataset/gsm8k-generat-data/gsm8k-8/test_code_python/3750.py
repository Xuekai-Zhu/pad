def solution():
    # Calculate the total number of accessories made
    total_accessories = 12000 * (2 + 3 + 1 + 5)

    # Calculate the total operation time for the accessories
    accessory_time = total_accessories * 10

    # Calculate the total operation time for the dolls
    doll_time = 12000 * 45

    # Calculate the combined operation time
    total_time = accessory_time + doll_time
    result = total_time
    return result

print(solution())