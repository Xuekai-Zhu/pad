def solution():
    """Heather made four times as many pizzas as Craig made on their first day at work at Mr. Pizza Inns. On their second day, Heather made 20 fewer pizzas than Craig's number. If Craig made 40 pizzas on their first day and 60 more pizzas on their second day than their first day, calculate the total number of pizzas the two made together in the two days."""
    craig_first_day = 40
    heather_first_day = craig_first_day * 4
    craig_second_day = craig_first_day + 60
    heather_second_day = craig_second_day - 20
    total_pizzas = craig_first_day + heather_first_day + craig_second_day + heather_second_day
    result = total_pizzas
    return result

print(solution())