def solution():
    miles_per_walk = 1.5  # Each walk is 1.5 miles
    walks_per_day = 2  # Clover goes for a walk in the morning and evening
    days = 30  # Clover walks for 30 days

    # Calculate the total miles walk in 30 days
    total_miles = miles_per_walk * walks_per_day * days
    result = total_miles
    return result

print(solution())