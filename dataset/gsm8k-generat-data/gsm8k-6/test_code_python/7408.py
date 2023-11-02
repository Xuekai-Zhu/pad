def solution():
    # Calculate the total rainfall during the storm
    total_rainfall = 5 + (5/2) + 0.5  # 5 inches in first 30 mins, half of that in the next 30 mins, and 0.5 inches in the next hour
    # Calculate the average rainfall per hour
    average_rainfall = total_rainfall / 2  # the storm lasted 2 hours
    result = average_rainfall
    return result

print(solution())