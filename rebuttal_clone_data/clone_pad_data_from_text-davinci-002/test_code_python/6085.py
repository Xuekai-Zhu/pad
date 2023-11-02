def solution():
    hours_filling = 5
    first_hour_fill_rate = 8
    second_hour_fill_rate = 10
    third_hour_fill_rate = 14
    fourth_hour_fill_rate = 0
    fifth_hour_fill_rate = -8
    total_fill = (first_hour_fill_rate + second_hour_fill_rate + third_hour_fill_rate + fourth_hour_fill_rate + fifth_hour_fill_rate) * hours_filling
    result = total_fill
    return result

print(solution())