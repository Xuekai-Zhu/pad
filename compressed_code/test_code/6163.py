def solution():
    
    points = [30, 28, 32, 34, 26]
    avg_points = sum(points) / len(points)
    if avg_points >= 30:
        total_pay = 10000
    else:
        total_pay = 8000
    result = total_pay
    return result

print(solution())