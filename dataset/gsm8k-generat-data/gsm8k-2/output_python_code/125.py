def solution():
    """Haley grows at the rate of 3 inches every year. If she is currently 20 inches tall, what will be her height after 10 years?"""
    current_height = 20
    growth_rate = 3
    time_years = 10
    final_height = current_height + (growth_rate * time_years)
    result = final_height
    return result

print(solution())