def solution():
    """Haley grows at the rate of 3 inches every year. If she is currently 20 inches tall, what will be her height after 10 years?"""
    rate_of_growth = 3
    current_height = 20
    years = 10
    new_height = current_height + (rate_of_growth * years)
    result = new_height
    return result

print(solution())