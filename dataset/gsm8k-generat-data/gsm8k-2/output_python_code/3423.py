def solution():
    """Larry spent $5 for lunch and gave his brother $2. How much did Larry have at the beginning if he has $15 now?"""
    lunch_cost = 5
    brother_receive = 2
    current_amount = 15
    initial_amount = current_amount + lunch_cost + brother_receive
    result = initial_amount
    return result

print(solution())