def solution():
    """Marjorie works as a baker. Every day, she makes twice as many cakes as she did the day before. On the sixth day, she makes 320 cakes. How many cakes did Marjorie make on the first day?"""
    # Working backwards from the sixth day to the first day
    day_6 = 320
    day_5 = day_6 / 2
    day_4 = day_5 / 2
    day_3 = day_4 / 2
    day_2 = day_3 / 2
    day_1 = day_2 / 2

    # Display the number of cakes Marjorie made on the first day
    result = day_1
    return result

print(solution())