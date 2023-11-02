def solution():
    """Carrie is trying to sneak some mashed turnips into her kids' mashed potatoes. She knows they didn't notice when she mixed 2 cups of turnips with 5 cups of potatoes. If she has 20 cups of potatoes, how many cups of turnips can she add?"""
    potatoes_available = 20
    turnips_to_potatoes_ratio = 2 / 5
    turnips_required = potatoes_available * turnips_to_potatoes_ratio
    result = turnips_required
    return result

print(solution())