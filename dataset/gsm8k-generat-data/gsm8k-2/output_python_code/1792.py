def solution():
    """It takes Dawn 2 hours to paint 1 watercolor painting. She was recently commissioned to paint a series of 12 paintings. Dawn will earn $3,600.00 for these 12 paintings. How much money does Dawn make per hour?"""
    hours_per_painting = 2
    total_paintings = 12
    total_payment = 3600
    payment_per_hour = total_payment / (total_paintings * hours_per_painting)
    result = payment_per_hour
    return result

print(solution())