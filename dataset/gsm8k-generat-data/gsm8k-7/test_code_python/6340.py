def solution():
    milk_per_milkshake = 4
    ice_cream_per_milkshake = 12
    total_milk = 72
    total_ice_cream = 192

    # Calculate the maximum number of milkshakes that Blake can make
    max_num_milkshakes = min(total_milk // milk_per_milkshake, total_ice_cream // ice_cream_per_milkshake)

    # Calculate the total amount of milk used for all the milkshakes
    total_milk_used = max_num_milkshakes * milk_per_milkshake

    # Calculate the amount of milk remaining
    milk_leftover = total_milk - total_milk_used
    result = milk_leftover
    return result

print(solution())