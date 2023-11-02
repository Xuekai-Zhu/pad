def solution():
    """Bobby has three squares of fabric that he will turn into a flag. The first square is 8 feet by 5 feet. The second one is 10 feet by 7 feet. The third one is 5 feet by 5 feet. If he wants his flag to be 15 feet long, how tall will it be?"""
    # Define the dimensions of the three squares of fabric
    square1_height = 8
    square1_width = 5
    square2_height = 10
    square2_width = 7
    square3_height = 5
    square3_width = 5

    # Define the desired length of the flag
    flag_length = 15

    # Calculate the total area of the fabric
    total_area = (square1_height * square1_width) + (square2_height * square2_width) + (square3_height * square3_width)

    # Calculate the required height of the flag to make it 15 feet long
    flag_height = total_area / flag_length

    # return the result
    result = flag_height
    return result

print(solution())