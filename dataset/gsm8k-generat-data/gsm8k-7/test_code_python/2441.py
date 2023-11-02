def solution():
    total_fish = 30
    blue_fish_frac = 1/3
    spotted_frac = 1/2

    # Calculate the number of blue fish
    blue_fish = total_fish * blue_fish_frac

    # Calculate the number of blue, spotted fish
    blue_spotted_fish = blue_fish * spotted_frac

    result = blue_spotted_fish
    return result

print(solution())