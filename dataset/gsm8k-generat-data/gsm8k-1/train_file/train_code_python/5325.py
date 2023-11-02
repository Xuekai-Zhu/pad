def solution():
    """Colin ran his first mile in 6 minutes. He ran his next two miles in 5 minutes each and finished his 4th mile in 4 minutes. What was the average time it took him to run a mile?"""
    total_minutes = 6 + 5 + 5 + 4
    total_miles = 4
    average_time_per_mile = total_minutes / total_miles
    result = average_time_per_mile
    return result

print(solution())