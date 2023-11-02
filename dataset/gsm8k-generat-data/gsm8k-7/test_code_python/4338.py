def solution():
    blue_ratio = 1/3
    spotted_ratio = 1/2
    num_spotted = 10

    # Calculate the total number of blue fish
    num_blue = num_spotted / spotted_ratio

    # Calculate the total number of fish in the tank
    total_fish = num_blue / blue_ratio
    result = total_fish
    return result

print(solution())