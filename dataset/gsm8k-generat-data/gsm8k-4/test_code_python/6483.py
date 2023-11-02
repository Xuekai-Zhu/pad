def solution():
    """Carrie is trying to sneak some mashed turnips into her kids' mashed potatoes. She knows they didn't notice when she mixed 2 cups of turnips with 5 cups of potatoes. If she has 20 cups of potatoes, how many cups of turnips can she add?"""
    # Calculate the ratio of turnips to potatoes in the original mixture
    turnip_ratio = 2 / 5

    # Calculate the number of cups of turnips needed for 20 cups of potatoes
    turnip_cups = turnip_ratio * 20

    # Return the result
    result = turnip_cups
    return result

print(solution())