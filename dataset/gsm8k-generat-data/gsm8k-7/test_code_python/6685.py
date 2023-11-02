def solution():
    craig_first_day = 40
    heather_first_day = 4 * craig_first_day
    craig_second_day = 60 + craig_first_day
    heather_second_day = craig_second_day - 20

    total_pizzas = craig_first_day + heather_first_day + craig_second_day + heather_second_day
    result = total_pizzas
    return result

print(solution())