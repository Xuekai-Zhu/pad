def solution():
    """Haley grows at the rate of 3 inches every year. If she is currently 20 inches tall, what will be her height after 10 years?"""
    growth_rate = 3
    current_height = 20
    years = 10
    height_after_ten_years = current_height + (growth_rate * years)
    result = height_after_ten_years
    return result

print(solution())