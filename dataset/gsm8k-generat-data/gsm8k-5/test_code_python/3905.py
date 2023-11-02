def solution():
    laps_per_day = 12  # Jasmine swims 12 laps every afternoon
    days_per_week = 5  # Jasmine swims Monday through Friday
    weeks = 5  # Jasmine wants to know how many laps she will swim in 5 weeks

    # Calculate the total number of laps Jasmine will swim in 5 weeks
    total_laps = laps_per_day * days_per_week * weeks
    result = total_laps
    return result

print(solution())