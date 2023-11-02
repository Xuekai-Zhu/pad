def solution():
    cost_of_gift = 250  # Cost of the gift they want to buy for their mother
    cost_of_cake = 25  # Cost of the birthday cake they want to buy for their mother
    total_cost = cost_of_gift + cost_of_cake  # Total cost of the gift and the cake

    # Calculate the total amount of money Erika and Rick have saved
    total_savings = 155 + (0.5 * cost_of_gift)

    # Calculate the amount of money they will have left after buying the gift and the cake
    left_over_money = total_savings - total_cost
    result = left_over_money
    return result

print(solution())