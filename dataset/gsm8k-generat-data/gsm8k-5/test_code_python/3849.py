def solution():
    lunch_cost = 10  # Randy spent $10 on lunch
    ice_cream_cost = 5  # The ice cream cone cost $5
    ice_cream_fraction = 0.25  # Randy spent a quarter of his remaining money on the ice cream cone

    # Calculate the total amount of money Randy spent
    total_spent = lunch_cost + ice_cream_cost

    # Calculate the amount of money Randy had left before buying the ice cream cone
    remaining_money = (total_spent / (1 - ice_cream_fraction)) - total_spent

    result = remaining_money
    return result

print(solution())