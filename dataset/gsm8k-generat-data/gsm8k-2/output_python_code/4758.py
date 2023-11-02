def solution():
    """James decides to buy himself a new barbell. It cost 30% more than his old $250 barbell. How much did it cost?"""
    old_barbell_cost = 250
    increase_percentage = 30
    new_barbell_cost = old_barbell_cost + (old_barbell_cost * (increase_percentage / 100))
    result = new_barbell_cost
    return result

print(solution())