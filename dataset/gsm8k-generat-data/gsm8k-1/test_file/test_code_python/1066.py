def solution():
    """Dennis uses 1 pound of butter for every dozen croissants that he makes.
    He needs to make 6 dozen croissants. The grocery store currently has a promotion 
    for buy one pound of butter get one half off. If the butter costs $4.00 a pound, how 
    much will it cost him to purchase 6 pounds of butter?"""
    croissants_per_dozen = 12
    dozens_needed = 6
    pounds_of_butter = dozens_needed * (1 / croissants_per_dozen)
    pounds_to_purchase = round(pounds_of_butter * (2/3), 2)
    cost_per_pound = 4.00
    total_cost = pounds_to_purchase * cost_per_pound
    result = total_cost
    return result

print(solution())