def solution():
    """John decides to buy some birds. He got 50 dollars from each of his 4 grandparents. If each bird costs $20, how many wings did all the birds have?"""
    grandparents_money = 4 * 50
    bird_cost = 20
    total_birds = grandparents_money // bird_cost
    total_wings = total_birds * 2
    result = total_wings
    return result

print(solution())