def solution():
    total_fish = 45
    male_ratio = 2/3

    # Calculate the number of male fish
    num_male_fish = total_fish * male_ratio

    # Calculate the number of female fish
    num_female_fish = total_fish - num_male_fish
    result = num_female_fish
    return result

print(solution())