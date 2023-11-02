def solution():
    # Craig's number of pizzas on first day
    craig_first_day = 40

    # Heather's number of pizzas on first day
    heather_first_day = 4*craig_first_day

    # Craig's number of pizzas on second day
    craig_second_day = craig_first_day + 60

    # Heather's number of pizzas on second day
    heather_second_day = craig_second_day - 20

    # Total pizzas made by Craig and Heather on first day
    total_first_day = craig_first_day + heather_first_day

    # Total pizzas made by Craig and Heather on second day
    total_second_day = craig_second_day + heather_second_day

    # Total number of pizzas made by Craig and Heather in two days
    total_pizzas = total_first_day + total_second_day

    result = total_pizzas
    return result

print(solution())