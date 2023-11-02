def solution():
    craig_first_day = 40  # Craig made 40 pizzas on the first day
    heather_first_day = 4 * craig_first_day  # Heather made four times as many pizzas as Craig on the first day
    craig_second_day = craig_first_day + 60  # Craig made 60 more pizzas on the second day
    heather_second_day = craig_second_day - 20  # Heather made 20 fewer pizzas than Craig on the second day

    # Calculate the total number of pizzas made in the two days
    total_pizzas = craig_first_day + heather_first_day + craig_second_day + heather_second_day
    result = total_pizzas
    return result

print(solution())