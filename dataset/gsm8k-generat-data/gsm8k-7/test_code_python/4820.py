def solution():
    num_bottles = 3
    total_volume = num_bottles

    # Calculate the volume of soda Danny drinks
    drank_volume = 0.9 * total_volume

    # Calculate the volume of soda Danny gives to his friends
    given_volume = 0.7 * (total_volume * (num_bottles - 1))

    # Calculate the remaining volume of soda Danny has
    remaining_volume = total_volume - drank_volume - given_volume

    # Calculate the remaining volume as a percentage of a bottle
    remaining_percent = (remaining_volume / total_volume) * 100
    result = remaining_percent
    return result

print(solution())