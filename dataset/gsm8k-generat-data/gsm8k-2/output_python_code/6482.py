def solution():
    """Carrie is trying to sneak some mashed turnips into her kids' mashed potatoes. She knows they didn't notice when she mixed 2 cups of turnips with 5 cups of potatoes. If she has 20 cups of potatoes, how many cups of turnips can she add?"""
    potato_to_turnip_ratio = 5 / 2
    potato_cups = 20
    turnip_cups = (potato_cups / potato_to_turnip_ratio) - potato_cups
    result = turnip_cups
    return result

print(solution())