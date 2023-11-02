def solution():
    """Wayne wants to serve shrimp cocktail as an appetizer. He plans on 5 shrimp per guest and will have 40 guests. If the shrimp costs $17.00 per pound and each pound has 20 shrimp, how much will he spend on the appetizer?"""
    shrimp_per_guest = 5
    total_guests = 40
    shrimp_per_pound = 20
    cost_per_pound = 17
    total_shrimp = shrimp_per_guest * total_guests
    pounds_of_shrimp = total_shrimp / shrimp_per_pound
    total_cost = pounds_of_shrimp * cost_per_pound
    result = total_cost
    return result

print(solution())