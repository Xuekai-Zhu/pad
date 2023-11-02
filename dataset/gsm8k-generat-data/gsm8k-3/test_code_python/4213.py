def solution():
    """Bobby has three squares of fabric that he will turn into a flag. The first square is 8 feet by 5 feet. The second one is 10 feet by 7 feet. The third one is 5 feet by 5 feet. If he wants his flag to be 15 feet long, how tall will it be?"""
    # Calculate the combined area of the three squares
    area = (8*5) + (10*7) + (5*5)

    # Calculate the height of the flag based on the given length of 15 feet
    height = area / 15

    # Display the height of the flag
    result = height
    return result

print(solution())