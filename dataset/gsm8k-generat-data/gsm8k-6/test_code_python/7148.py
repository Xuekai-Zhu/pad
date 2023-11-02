def solution():
    # Calculate the total number of fish added over the three weeks
    koi_added = 2 * 7 * 3  # 2 koi fish added per day over 3 weeks (21 days)
    goldfish_added = 5 * 7 * 3  # 5 goldfish added per day over 3 weeks (21 days)

    # Calculate the total number of koi fish in the tank before the three weeks
    total_fish = 280 - koi_added - goldfish_added
    koi_fish = total_fish - 200  # if there were 200 goldfish, then the rest must be koi fish
    result = koi_fish
    return result

print(solution())