def solution():
    # Define the cost of the new computer and Troy's savings
    new_computer_cost = 80
    troy_savings = 50

    # Calculate the amount from selling the old computer
    old_computer_sale = 20

    # Calculate the total amount Troy has
    total_money = troy_savings + old_computer_sale

    # Calculate the amount Troy still needs to buy the new computer
    remaining_cost = new_computer_cost - total_money
    result = remaining_cost
    return result

print(solution())