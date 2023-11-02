def solution():
    total_fish = 280  # The tank has a total of 280 fish
    added_koi_per_day = 2  # The school adds 2 koi fish per day
    added_goldfish_per_day = 5  # The school adds 5 goldfish per day
    weeks = 3  # The school adds fish for 3 weeks

    # Calculate the total number of fish added over the 3 weeks
    total_added_koi = added_koi_per_day * 7 * weeks  # 7 days per week
    total_added_goldfish = added_goldfish_per_day * 7 * weeks

    # Calculate the total number of goldfish after the 3 weeks
    total_goldfish = 200
    total_koi = total_fish - total_goldfish  # The remaining fish are koi fish

    # Calculate the initial number of koi fish
    initial_koi = total_koi - total_added_koi

    # Calculate the total number of koi fish after the 3 weeks
    total_koi_after_3_weeks = initial_koi + total_added_koi
    result = total_koi_after_3_weeks
    return result

print(solution())