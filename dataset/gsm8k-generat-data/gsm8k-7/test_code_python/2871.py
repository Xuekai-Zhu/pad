def solution():
    cabin_cost = 129000
    cash_on_hand = 150

    # Calculate the total value of all trees
    num_cypress = 20
    cypress_value = 100
    total_cypress_value = num_cypress * cypress_value

    num_maple = 24
    maple_value = 300
    total_maple_value = num_maple * maple_value

    num_pine = 600
    pine_value = 200
    total_pine_value = num_pine * pine_value

    total_tree_value = total_cypress_value + total_maple_value + total_pine_value

    # Calculate the remaining amount of money after paying for the cabin
    remaining_money = cash_on_hand + (total_tree_value - cabin_cost)
    result = remaining_money
    return result

print(solution())