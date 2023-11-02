def solution():
    initial_guppies = 7  # Amber starts with 7 guppies
    baby_guppies_first_day = 3 * 12  # 3 dozen baby guppies seen on the first day
    baby_guppies_second_day = 9  # 9 more baby guppies seen on the second day

    # Calculate the total number of guppies Amber has now
    total_guppies = initial_guppies + baby_guppies_first_day + baby_guppies_second_day
    result = total_guppies
    return result

print(solution())