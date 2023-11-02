def solution():
    
    hours_per_painting = 2
    total_paintings = 12
    total_payment = 3600
    payment_per_hour = total_payment / (total_paintings * hours_per_painting)
    result = payment_per_hour
    return result

print(solution())