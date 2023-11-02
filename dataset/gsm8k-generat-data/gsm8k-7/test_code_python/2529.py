def solution():
    competitor_1_rate = 10  # hot dogs per minute
    competitor_2_rate = competitor_1_rate * 3  # hot dogs per minute
    competitor_3_rate = competitor_2_rate * 2  # hot dogs per minute
    num_minutes = 5

    # Calculate the total number of hot dogs eaten by each competitor
    competitor_1_total = competitor_1_rate * num_minutes
    competitor_2_total = competitor_2_rate * num_minutes
    competitor_3_total = competitor_3_rate * num_minutes

    # Return the total hot dogs eaten by competitor 3
    result = competitor_3_total
    return result

print(solution())