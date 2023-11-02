def solution():
    """Simeon drinks 64 fluid ounces of filtered water every day. He used to drink this water in 8-ounce-servings. But now, he drinks his water in 16-ounce servings. How many fewer servings per day does it now take Simeon to drink his water than it used to?"""
    total_water = 64
    old_servings = total_water / 8
    new_servings = total_water / 16
    difference = old_servings - new_servings
    result = difference
    return result

print(solution())