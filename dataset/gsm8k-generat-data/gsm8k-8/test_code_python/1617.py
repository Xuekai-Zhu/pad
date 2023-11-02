def solution():
    # Define the cost per ingredient in cents
    bread_cost = 15
    ham_cost = 25
    cheese_cost = 35

    # Calculate the total cost of one sandwich
    sandwich_cost = bread_cost * 2 + ham_cost + cheese_cost

    # Convert the total cost to dollars
    sandwich_cost = sandwich_cost / 100

    # Calculate the profit per sandwich
    profit = 1.50 - sandwich_cost

    # Convert the profit to cents
    profit = profit * 100

    result = sandwich_cost
    return result

print(solution())