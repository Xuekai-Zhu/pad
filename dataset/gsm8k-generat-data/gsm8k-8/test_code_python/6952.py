def solution():
    # Calculate the cost of the hamburger meat
    hamburger_cost = 2 * 3.5

    # Calculate the total cost of the groceries
    total_cost = hamburger_cost + 1.5 + 1 + 2 * 2 - 1

    # Calculate how much Lauren pays with a $20 bill
    paid = 20

    # Calculate the change Lauren gets back
    change = paid - total_cost
    result = change
    return result

print(solution())