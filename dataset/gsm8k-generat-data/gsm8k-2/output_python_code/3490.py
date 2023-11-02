def solution():
    """Half of Taylor's house guests like weak coffee and the other half like strong coffee in the morning. Taylor uses 1 tablespoon of coffee per cup of water to make it weak and he doubles that amount to make it strong. If he makes 12 cups of both weak and strong coffee, how many tablespoons of coffee will he need?"""
    cups_per_type = 12
    weak_coffee_ratio = 0.5
    strong_coffee_ratio = 0.5
    weak_coffee_intensity = 1
    strong_coffee_intensity = weak_coffee_intensity * 2
    total_coffee = (cups_per_type * weak_coffee_ratio * weak_coffee_intensity) + (cups_per_type * strong_coffee_ratio * strong_coffee_intensity)
    result = total_coffee
    return result

print(solution())