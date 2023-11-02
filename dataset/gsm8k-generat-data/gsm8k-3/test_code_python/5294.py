def solution():
    """Allie picked 44 wildflowers.  Thirteen of the flowers were yellow and white, seventeen of the flowers were red and yellow, and 14 of the flowers were red and white.  How many more flowers contained the color red than contained the color white?"""
    # Define the number of flowers of each color combination
    YW_FLOWERS = 13
    RY_FLOWERS = 17
    RW_FLOWERS = 14

    # Calculate the number of red flowers and white flowers
    red_flowers = RY_FLOWERS + RW_FLOWERS
    white_flowers = YW_FLOWERS + RW_FLOWERS

    # Calculate the difference between the number of red and white flowers
    diff = red_flowers - white_flowers

    # Display the result
    result = diff
    return result

print(solution())