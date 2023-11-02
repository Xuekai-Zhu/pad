def solution():
    num_jeffery_fish = 60
    num_ryan_fish = num_jeffery_fish / 2
    num_jason_fish = num_ryan_fish / 3

    # Calculate the total number of fish caught by all of them
    total_fish = num_jeffery_fish + num_ryan_fish + num_jason_fish
    result = total_fish
    return result

print(solution())