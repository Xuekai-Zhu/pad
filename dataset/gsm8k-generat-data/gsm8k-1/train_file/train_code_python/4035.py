def solution():
    """Marjorie works as a baker. Every day, she makes twice as many cakes as she did the day before. On the sixth day, she makes 320 cakes. How many cakes did Marjorie make on the first day?"""
    day_six_cakes = 320
    cakes_on_fifth_day = day_six_cakes / 2
    cakes_on_fourth_day = cakes_on_fifth_day / 2
    cakes_on_third_day = cakes_on_fourth_day / 2
    cakes_on_second_day = cakes_on_third_day / 2
    cakes_on_first_day = cakes_on_second_day / 2
    result = cakes_on_first_day
    return result

print(solution())