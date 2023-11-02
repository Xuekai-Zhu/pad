def solution():
    """James decides to buy himself a new barbell. It cost 30% more than his old $250 barbell. How much did it cost?"""
    old_barbell_cost = 250
    percent_increase = 30
    increase_amount = old_barbell_cost * (percent_increase / 100)
    new_barbell_cost = old_barbell_cost + increase_amount
    result = new_barbell_cost
    return result

print(solution())