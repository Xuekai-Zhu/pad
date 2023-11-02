def solution():
    first_day = 45
    second_day = first_day + 20
    third_day = 2*second_day - 10
    total_daisies = 350
    sold_on_fourth_day = total_daisies - first_day - second_day - third_day
    result = sold_on_fourth_day
    return result

print(solution())