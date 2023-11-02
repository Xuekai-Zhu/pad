def solution():
    """ Carrie is trying to sneak some mashed turnips into her kids' mashed potatoes. She knows they didn't notice when she mixed 2 cups of turnips with 5 cups of potatoes. If she has 20 cups of potatoes, how many cups of turnips can she add? """
    # Calculate the ratio of turnips to potatoes in the original mixture
    turnip_potato_ratio = 2 / 5

    # Calculate how many cups of turnips are needed to maintain the same ratio
    cups_of_turnips = turnip_potato_ratio * 20

    # Display the number of cups of turnips needed
    result = cups_of_turnips
    return result

print(solution())