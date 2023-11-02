def solution():
    """Bobby has three squares of fabric that he will turn into a flag. The first square is 8 feet by 5 feet. The second one is 10 feet by 7 feet. The third one is 5 feet by 5 feet. If he wants his flag to be 15 feet long, how tall will it be?"""
    first_square_area = 8 * 5
    second_square_area = 10 * 7
    third_square_area = 5 * 5
    total_area = first_square_area + second_square_area + third_square_area
    height = total_area / 15
    result = height
    return result

print(solution())