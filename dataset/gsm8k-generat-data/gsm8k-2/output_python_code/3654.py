def solution():
    """To make a lasagna Martha needs 1.5kg of cheese and 500 grams of meat. The cheese costs $6 per kilogram, and the meat $8 per kilogram. How much does Martha need to pay for the ingredients?"""
    cheese_weight = 1.5
    cheese_price_per_kg = 6
    meat_weight = 0.5
    meat_price_per_kg = 8
    cheese_cost = cheese_weight * cheese_price_per_kg
    meat_cost = meat_weight * meat_price_per_kg
    total_cost = cheese_cost + meat_cost
    result = total_cost
    return result

print(solution())