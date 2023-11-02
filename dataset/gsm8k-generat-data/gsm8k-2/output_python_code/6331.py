def solution():
    """Lillian went out to forage for mushrooms with her handy guidebook. She found 32 mushrooms and used her guidebook to identify which ones were poisonous and which were safe to eat. In the end, she had 9 mushrooms she could safely eat for dinner. Of the rest, she identified twice the amount she ate as poisonous, and a remaining bunch she was uncertain about. How many mushrooms was she uncertain were safe or poisonous?"""
    total_mushrooms = 32
    safe_mushrooms = 9
    eaten_mushrooms = total_mushrooms - safe_mushrooms
    poisonous_mushrooms = 2 * eaten_mushrooms
    uncertain_mushrooms = total_mushrooms - safe_mushrooms - poisonous_mushrooms
    result = uncertain_mushrooms
    return result

print(solution())