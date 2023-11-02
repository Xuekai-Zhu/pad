def solution():
    """Heather made four times as many pizzas as Craig made on their first day at work at Mr. Pizza Inns. On their second day, Heather made 20 fewer pizzas than Craig's number. If Craig made 40 pizzas on their first day and 60 more pizzas on their second day than their first day, calculate the total number of pizzas the two made together in the two days."""
    # Calculate how many pizzas Heather made on the first day
    craig_pizzas = 40
    heather_pizzas = craig_pizzas * 4

    # Calculate how many pizzas Craig made on the second day
    craig_pizzas_2 = craig_pizzas + 60

    # Calculate how many pizzas Heather made on the second day
    heather_pizzas_2 = craig_pizzas_2 - 20

    # Calculate the total number of pizzas made over the two days
    total_pizzas = craig_pizzas + heather_pizzas + craig_pizzas_2 + heather_pizzas_2

    # Display the total number of pizzas
    result = total_pizzas
    return result

print(solution())