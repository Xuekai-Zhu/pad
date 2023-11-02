def solution():
    num_fish = 6
    days = [3, 5, 7]
    removed_fish = [1/3, 1/4]
    added_fish = 15

    # Calculate the number of fish after doubling for each day
    for day in days:
        num_fish *= 2

        # If it's the third day, remove one-third of the fish
        if day == 3:
            num_fish -= num_fish * removed_fish[0]

        # If it's the fifth day, remove one-fourth of the fish
        if day == 5:
            num_fish -= num_fish * removed_fish[1]

        # If it's the seventh day, add 15 more fish
        if day == 7:
            num_fish += added_fish

    result = num_fish
    return result

print(solution())