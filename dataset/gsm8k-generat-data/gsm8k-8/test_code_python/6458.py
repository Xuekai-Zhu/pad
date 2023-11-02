def solution():
    # Calculate the cost of 10 buns
    bun_cost = 10 * 0.1

    # Calculate the cost of two bottles of milk
    milk_cost = 2 * 2

    # Calculate the cost of one bottle of milk
    one_milk_cost = milk_cost / 2

    # Calculate the cost of the carton of eggs
    egg_cost = one_milk_cost * 3

    # Calculate the total cost of Frank's breakfast shopping
    total_cost = bun_cost + milk_cost + egg_cost

    result = total_cost
    return result

print(solution())