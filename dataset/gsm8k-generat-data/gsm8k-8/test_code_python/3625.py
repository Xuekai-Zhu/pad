def solution():
    # Define the cost of one pound of steak and the amount Ken buys 
    cost_per_pound = 7
    amount_bought = 2

    # Calculate the total cost of the steak
    total_cost = cost_per_pound * amount_bought

    # Calculate the amount Ken pays and how much he gets back
    amount_paid = 20
    change = amount_paid - total_cost
    result = change
    return result

print(solution())