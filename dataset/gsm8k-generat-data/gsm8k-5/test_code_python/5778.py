def solution():
    daily_hours = 2  # Carl drives 2 hours every day
    extra_hours = 6  # After getting promoted, Carl has to drive 6 more hours every week
    weeks = 2  # Carl wants to know how many hours he will drive in 2 weeks

    # Calculate the total number of hours Carl will drive in 2 weeks
    total_hours = daily_hours * 14 + extra_hours * 2  # 14 days in 2 weeks, and 2 extra hours per week for promotion

    result = total_hours
    return result

print(solution())