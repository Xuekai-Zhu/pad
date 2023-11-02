def solution():
    """Marjorie works as a baker. Every day, she makes twice as many cakes as she did the day before. On the sixth day, she makes 320 cakes. How many cakes did Marjorie make on the first day?"""
    total_cakes = 320
    current_day_cakes = total_cakes
    for day in range(6, 0, -1):
        current_day_cakes /= 2
        if day == 1:
            result = current_day_cakes
    return result

print(solution())