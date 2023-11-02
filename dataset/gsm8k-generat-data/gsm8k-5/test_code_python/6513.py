def solution():
    fish_per_hour = 7
    hours_fished = 9

    # Calculate the total number of fish caught before losing any
    total_fish = fish_per_hour * hours_fished

    # Subtract the number of fish lost
    total_fish -= 15

    result = total_fish
    return result

print(solution())