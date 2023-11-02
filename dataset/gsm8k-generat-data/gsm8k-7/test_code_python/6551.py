def solution():
    new_comp_price = 80
    initial_savings = 50
    old_comp_price = 20

    # Calculate the total amount of money Troy has
    total_money = initial_savings + old_comp_price

    # Calculate the remaining amount of money Troy needs to buy the new computer
    remaining_money = new_comp_price - total_money
    result = remaining_money
    return result

print(solution())