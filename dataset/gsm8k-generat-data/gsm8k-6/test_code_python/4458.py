def solution():
    # Calculate the total hours the business is open in a week
    weekday_hours = (10 - 4) * 5  # Monday through Friday, from 4 pm to 10 pm
    weekend_hours = (10 - 6) * 2  # Saturday and Sunday, from 6 pm to 10 pm
    total_hours = weekday_hours + weekend_hours
    result = total_hours
    return result

print(solution())