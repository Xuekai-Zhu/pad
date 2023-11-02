def solution():
    
    total_points = 30 + 28 + 32 + 34 + 26
    average_points = total_points / 5
    if average_points >= 30:
        payment = 10000
    else:
        payment = 8000
    result = payment
    return result

print(solution())