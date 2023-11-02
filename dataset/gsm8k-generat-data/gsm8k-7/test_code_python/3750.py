def solution():
    num_dolls = 12000
    num_shoes_per_doll = 2
    num_bags_per_doll = 3
    num_cosmetics_per_doll = 1
    num_hats_per_doll = 5
    doll_time = 45  # seconds
    accessory_time = 10  # seconds

    # Calculate the total time required to make all the dolls
    total_doll_time = num_dolls * doll_time

    # Calculate the total time required to make all the accessories
    total_accessory_time = (num_shoes_per_doll + num_bags_per_doll + num_cosmetics_per_doll + num_hats_per_doll) * num_dolls * accessory_time

    # Calculate the total time required for both dolls and accessories
    total_time = total_doll_time + total_accessory_time
    result = total_time
    return result

print(solution())