def solution():
    # Calculate the amount spent on groceries
    groceries = 2 * 12 + 12  # bought apples, butter, eggs, and a large ham for twice the cost of the toilet paper

    # Calculate the amount of money left after buying toilet paper and groceries
    total_spent = 12 + groceries
    leftover_money = 50 - total_spent

    # Calculate the cost of one pair of boots
    cost_per_boot = 3 * leftover_money

    # Calculate the total cost of two pairs of boots
    total_boots_cost = 2 * cost_per_boot

    # Calculate the amount each twin has to add to buy two pairs of boots
    amount_to_add = total_boots_cost / 2

    result = amount_to_add
    return result

print(solution())