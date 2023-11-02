def solution():
    """Adam bought 3 kilograms of nuts and 2.5 kilograms of dried fruits at a store. One kilogram of nuts costs $12 and one kilogram of dried fruit costs $8. How much did his purchases cost?"""
    nuts_kg = 3
    dried_fruit_kg = 2.5
    nut_cost_per_kg = 12
    fruit_cost_per_kg = 8
    total_cost = (nuts_kg * nut_cost_per_kg) + (dried_fruit_kg * fruit_cost_per_kg)
    result = total_cost
    return result

print(solution())