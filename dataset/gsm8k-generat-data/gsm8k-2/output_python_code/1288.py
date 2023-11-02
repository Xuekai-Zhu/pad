def solution():
    """Gary has 30 grams of gold that cost $15 per gram. Anna has 50 grams of gold for the cost of $20 per gram. How much is the cost of their gold combined?"""
    gary_gold_grams = 30
    gary_gold_price = 15
    anna_gold_grams = 50
    anna_gold_price = 20
    gary_gold_cost = gary_gold_grams * gary_gold_price
    anna_gold_cost = anna_gold_grams * anna_gold_price
    total_cost = gary_gold_cost + anna_gold_cost
    result = total_cost
    return result

print(solution())