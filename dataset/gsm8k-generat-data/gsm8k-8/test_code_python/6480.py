def solution():
    # Define the given information
    total_mugs = 40
    yellow_mugs = 12
    red_mugs = 0.5 * yellow_mugs
    blue_mugs = 3 * red_mugs

    # Calculate the number of mugs in the mentioned colors
    mentioned_mugs = yellow_mugs + red_mugs + blue_mugs

    # Calculate the number of mugs in other colors
    other_mugs = total_mugs - mentioned_mugs
    result = other_mugs
    return result

print(solution())