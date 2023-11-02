def solution():
    """Alexis is applying for a new job and bought a new set of business clothes to wear to the interview. She went to a department store with a budget of $200 and spent $30 on a button-up shirt, $46 on suit pants, $38 on a suit coat, $11 on socks, and $18 on a belt. She also purchased a pair of shoes, but lost the receipt for them. She has $16 left from her budget. How much did Alexis pay for the shoes?"""
    # Define the total budget and the cost of the clothes purchased
    total_budget = 200
    total_cost = 30 + 46 + 38 + 11 + 18

    # Calculate the amount of money left from the budget
    money_left = total_budget - total_cost

    # Assume the cost of shoes is equal to the money left
    shoes_cost = money_left

    result = shoes_cost
    return result

print(solution())