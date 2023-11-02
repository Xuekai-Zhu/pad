def solution():
    num_pills = 50
    pills_per_day = 6  # 2 pills, 3 times a day
    days_at_full_dose = 2
    days_at_half_dose = 3

    # Calculate the total number of pills taken during the first two days
    pills_during_full_dose = pills_per_day * days_at_full_dose

    # Calculate the total number of pills taken during the next three days
    pills_during_half_dose = (pills_per_day / 2) * days_at_half_dose

    # Calculate the total number of pills taken during the sixth day
    pills_on_last_day = 2

    # Calculate the total number of pills taken over the six days
    total_pills_taken = pills_during_full_dose + pills_during_half_dose + pills_on_last_day

    # Calculate the number of pills left in the bottle
    pills_left = num_pills - total_pills_taken
    result = pills_left
    return result

print(solution())