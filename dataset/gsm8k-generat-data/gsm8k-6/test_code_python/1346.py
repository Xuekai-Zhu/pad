def solution():
    # Calculate the number of brown toads per acre
    spotted_browns_per_acre = 50
    total_browns_per_acre = spotted_browns_per_acre * 4  # one-quarter of the brown toads are spotted
    total_toads_per_acre = total_browns_per_acre + total_browns_per_acre // 25  # for every green toad, there are 25 brown toads
    green_toads_per_acre = total_toads_per_acre // 26  # there are 26 toads (1 green and 25 browns) for every group
    result = green_toads_per_acre
    return result

print(solution())