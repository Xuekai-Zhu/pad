def solution():
    """Victoria was given a $50 bill by her mother to buy her friends snacks for their group meeting. She bought 2 boxes of pizza that costs $12 each and 2 packs of juice drinks that cost $2 each. How much money should Victoria return to her mother?"""
    bill_amount = 50
    pizza_cost = 12
    juice_cost = 2
    total_cost = (2 * pizza_cost) + (2 * juice_cost)
    change_amount = bill_amount - total_cost
    result = change_amount
    return result

print(solution())