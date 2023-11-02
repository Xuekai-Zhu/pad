def solution():
    total_fish = 280
    added_koi_per_day = 2
    added_goldfish_per_day = 5
    num_days = 21   # 3 weeks = 21 days
    ending_goldfish = 200

    # Calculate the initial number of koi fish by subtracting the initial number of goldfish
    initial_koi = total_fish - ending_goldfish

    # Calculate the total number of koi fish added over the three weeks
    total_koi_added = added_koi_per_day * num_days

    # Calculate the total number of koi fish in the tank after the three weeks
    total_koi = initial_koi + total_koi_added
    result = total_koi
    return result

print(solution())