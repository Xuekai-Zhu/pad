def solution():
    """It takes Dawn 2 hours to paint 1 watercolor painting. She was recently commissioned to paint a series of 12 paintings. Dawn will earn $3,600.00 for these 12 paintings. How much money does Dawn make per hour?"""
    paintings = 12
    time_per_painting = 2
    total_time = paintings * time_per_painting
    money_earned = 3600
    money_per_hour = money_earned / total_time
    result = money_per_hour
    return result

print(solution())