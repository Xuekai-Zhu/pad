def solution():
    total_pills = 50  # Tony buys a bottle of 50 pills
    pills_per_day = 2  # Tony takes 2 pills three times a day
    days_first_dose = 2  # Tony takes this dose for the first 2 days
    days_second_dose = 3  # Tony takes a half dose for the next 3 days

    # Calculate the total number of pills Tony takes in the first 2 days
    pills_first_dose = pills_per_day * 3 * days_first_dose

    # Calculate the total number of pills Tony takes in the next 3 days
    pills_second_dose = (pills_per_day / 2) * 3 * days_second_dose

    # Calculate the total number of pills Tony takes in the last day
    pills_last_day = pills_per_day

    # Calculate the total number of pills taken by Tony
    total_pills_taken = pills_first_dose + pills_second_dose + pills_last_day

    # Calculate the number of pills left in the bottle
    pills_left = total_pills - total_pills_taken
    result = pills_left
    return result

print(solution())