def solution():
    """John decides to buy some birds. He got 50 dollars from each of his 4 grandparents. If each bird costs $20, how many wings did all the birds have?"""
    money_from_grandparents = 50 * 4
    cost_per_bird = 20
    total_birds = money_from_grandparents // cost_per_bird
    total_wings = total_birds * 2
    result = total_wings
    return result

print(solution())