def solution():
    # Calculate the number of blue mugs and red mugs Hannah has
    yellow_mugs = 12
    red_mugs = yellow_mugs // 2  # Hannah has only half as many red mugs as yellow mugs
    blue_mugs = 3 * red_mugs  # Hannah has three times more blue mugs than red mugs

    # Calculate the total number of mugs Hannah has, including the other color mugs
    total_mugs = yellow_mugs + red_mugs + blue_mugs + 40

    # Calculate the number of mugs of another color than mentioned Hannah has
    other_color_mugs = total_mugs - (yellow_mugs + red_mugs + blue_mugs + 40)

    result = other_color_mugs
    return result

print(solution())