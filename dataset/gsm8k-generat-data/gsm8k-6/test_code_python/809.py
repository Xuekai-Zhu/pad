def solution():
    # Calculate the total number of miles Clover walks in 30 days
    miles_per_day = 1.5 + 1.5  # Clover walks 1.5 miles in the morning and 1.5 miles in the evening every day
    total_miles = miles_per_day * 30  # multiply by 30 days
    result = total_miles
    return result

print(solution())