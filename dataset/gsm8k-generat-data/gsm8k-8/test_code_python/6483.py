def solution():
    # Calculate the ratio of turnips to potatoes in the original mixture
    original_ratio = 2/5

    # Calculate the amount of turnips in the original mixture
    original_turnips = original_ratio * 5

    # Calculate the ratio of turnips to potatoes for the new mixture
    new_ratio = original_turnips / 5

    # Calculate the amount of turnips needed for the new mixture
    new_turnips = new_ratio * 20

    result = new_turnips
    return result

print(solution())