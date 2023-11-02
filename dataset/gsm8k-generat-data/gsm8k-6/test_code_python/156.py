def solution():
    # Calculate the cost of the sandwich
    sandwich_cost = 4

    # Calculate the cost of the juice
    juice_cost = 2 * sandwich_cost

    # Calculate the total cost of the sandwich and juice
    sandwich_and_juice_cost = sandwich_cost + juice_cost

    # Calculate the cost of the milk
    milk_cost = 0.75 * sandwich_and_juice_cost

    # Calculate the total cost of the food purchased by George
    total_cost = sandwich_cost + juice_cost + milk_cost

    result = total_cost
    return result

print(solution())