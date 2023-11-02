def solution():
    """Sherry is making banana bread for a bake sale. She wants to make 99 loaves. Her recipe makes enough batter for 3 loaves. The recipe calls for 1 banana. How many bananas does Sherry need?"""
    loaves_per_recipe = 3
    total_loaves = 99
    bananas_per_recipe = 1
    total_bananas = (total_loaves // loaves_per_recipe) * bananas_per_recipe
    result = total_bananas
    return result

print(solution())