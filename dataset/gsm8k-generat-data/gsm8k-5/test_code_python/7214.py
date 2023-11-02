def solution():
    starting_money = 40  # Phil started with $40
    pizza_cost = 2.75
    soda_cost = 1.50
    jeans_cost = 11.50

    # Calculate how much money Phil has left after buying pizza, soda, and jeans
    remaining_money = starting_money - (pizza_cost + soda_cost + jeans_cost)

    # Calculate the number of quarters Phil has based on his remaining money
    num_quarters = int(remaining_money / 0.25)

    result = num_quarters
    return result

print(solution())