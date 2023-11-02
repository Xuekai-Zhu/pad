def solution():
    """Jeff orders a Halloween costume. He has to put in a 10% deposit and then pay the rest when he picks it up. The costume is 40% more expensive than last year's costume, which cost $250. How much did he pay when picking it up, in dollars?"""
    deposit_percent = 10
    last_year_cost = 250
    percent_increase = 40
    deposit_amount = last_year_cost * (deposit_percent / 100)
    total_cost = last_year_cost * (1 + (percent_increase / 100))
    rest_due = total_cost - deposit_amount
    result = rest_due
    return result

print(solution())