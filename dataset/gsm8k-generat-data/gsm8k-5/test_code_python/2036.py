def solution():
    total_days = 30  # Mr. Johnson has a prescription for 30 days
    days_taken = total_days * (4/5)  # Mr. Johnson has already taken 4/5 of the days
    days_left = total_days - days_taken  # Mr. Johnson has 1/5 of the days left
    pills_left = 12  # Mr. Johnson has 12 pills left after 4/5 of the days

    # Calculate the total number of pills Mr. Johnson should have taken by now
    total_pills_needed = (total_days - days_left) * pills_left

    # Calculate the number of pills Mr. Johnson should take daily
    pills_per_day = total_pills_needed / days_taken
    result = pills_per_day
    return result

print(solution())