def solution():
    """Gary has 30 grams of gold that cost $15 per gram. Anna has 50 grams of gold for the cost of $20 per gram. How much is the cost of their gold combined?"""
    gary_grams = 30
    gary_cost_per_gram = 15
    gary_cost = gary_grams * gary_cost_per_gram
    anna_grams = 50
    anna_cost_per_gram = 20
    anna_cost = anna_grams * anna_cost_per_gram
    total_cost = gary_cost + anna_cost
    result = total_cost
    return result

print(solution())