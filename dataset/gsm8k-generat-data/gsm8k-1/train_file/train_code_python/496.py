def solution():
    """James's favorite basketball player got paid based on how many points he averaged each week. He gets $10,000 if he averages 30 or more points a game and $8,000 if he averages under 30 points a game. For his last week, in the first game he scored 30 points and in the second game he scored 28 points. In the third game he scored 32 points. In the fourth game he scored 34 points and in the fifth game he scored 26 points. How much does he get paid for the week?"""
    points = [30, 28, 32, 34, 26]
    avg_points = sum(points) / len(points)
    if avg_points >= 30:
        total_pay = 10000
    else:
        total_pay = 8000
    result = total_pay
    return result

print(solution())