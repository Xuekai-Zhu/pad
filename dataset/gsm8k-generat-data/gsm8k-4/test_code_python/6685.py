def solution():
    """Heather made four times as many pizzas as Craig made on their first day at work at Mr. Pizza Inns. On their second day, Heather made 20 fewer pizzas than Craig's number. If Craig made 40 pizzas on their first day and 60 more pizzas on their second day than their first day, calculate the total number of pizzas the two made together in the two days."""
    # Calculate the number of pizzas Heather made on the first day
    heather_first_day = 4 * 40

    # Calculate the number of pizzas Craig made on the second day
    craig_second_day = 40 + 60

    # Calculate the total number of pizzas made by both on the second day
    total_second_day = heather_second_day + craig_second_day

    # Calculate the total number of pizzas made by both in the two days
    total_pizzas = heather_first_day + craig_first_day + total_second_day

    # return the result
    result = total_pizzas
    return result

print(solution())