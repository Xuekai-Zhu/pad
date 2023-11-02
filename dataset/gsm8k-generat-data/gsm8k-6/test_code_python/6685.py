def solution():
    # Calculate the number of pizzas Heather made on the first day
    pizzas_Heather_day1 = 4 * 40  # Heather made four times as many pizzas as Craig made, Craig made 40 pizzas on their first day

    # Calculate the number of pizzas Craig made on the second day
    pizzas_Craig_day2 = 40 + 60  # Craig made 60 more pizzas on their second day than their first day

    # Calculate the total number of pizzas made by both of them in two days
    total_pizzas = pizzas_Heather_day1 + pizzas_Craig_day2 - 20  # Heather made 20 fewer pizzas than Craig's number on their second day
    result = total_pizzas
    return result

print(solution())