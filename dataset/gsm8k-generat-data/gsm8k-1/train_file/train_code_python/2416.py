def solution():
    """Simeon drinks 64 fluid ounces of filtered water every day. He used to drink this water in 8-ounce-servings. But now, he drinks his water in 16-ounce servings. How many fewer servings per day does it now take Simeon to drink his water than it used to?"""
    total_fluid_ounces = 64
    old_serving_size = 8
    new_serving_size = 16
    old_servings = total_fluid_ounces / old_serving_size
    new_servings = total_fluid_ounces / new_serving_size
    fewer_servings = old_servings - new_servings
    result = fewer_servings
    return result

print(solution())