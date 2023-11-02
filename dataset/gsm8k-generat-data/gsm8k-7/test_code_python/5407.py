def solution():
    day1_hours = 2
    day2_hours = day1_hours * 2
    day3_hours = day2_hours - 1

    # Calculate the total minutes studied on day 1
    day1_minutes = day1_hours * 60

    # Calculate the total minutes studied on day 2
    day2_minutes = day2_hours * 60

    # Calculate the total minutes studied on day 3
    day3_minutes = day3_hours * 60

    # Calculate the total minutes studied over the 3 days
    total_minutes = day1_minutes + day2_minutes + day3_minutes
    result = total_minutes
    return result

print(solution())