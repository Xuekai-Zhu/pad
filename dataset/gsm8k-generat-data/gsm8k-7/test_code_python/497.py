def solution():
    points = [30, 28, 32, 34, 26]
    avg_points = sum(points) / len(points)

    if avg_points >= 30:
        pay = 10000
    else:
        pay = 8000

    result = pay
    return result

print(solution())