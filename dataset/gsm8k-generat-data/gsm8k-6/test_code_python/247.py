def solution():
    # Calculate the number of pills Tony takes in the first 2 days
    pills_first_2_days = 2 * 3 * 2  # 2 pills each time, 3 times a day, for 2 days

    # Calculate the number of pills Tony takes in the next 3 days
    pills_next_3_days = 2 * 3 * 0.5  # 2 pills each time, 3 times a day, halved, for 3 days

    # Calculate the total number of pills Tony takes
    total_pills_taken = pills_first_2_days + pills_next_3_days + 2  # adding the 2 pills taken on the sixth day

    # Calculate the number of pills left in the bottle
    pills_left = 50 - total_pills_taken
    result = pills_left
    return result

print(solution())