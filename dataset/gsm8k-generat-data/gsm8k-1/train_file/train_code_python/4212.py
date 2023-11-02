def solution():
    """Bobby has three squares of fabric that he will turn into a flag. The first square is 8 feet by 5 feet. The second one is 10 feet by 7 feet. The third one is 5 feet by 5 feet. If he wants his flag to be 15 feet long, how tall will it be?"""
    length1 = 8
    width1 = 5
    length2 = 10
    width2 = 7
    length3 = 5
    width3 = 5
    
    # Finding the total area of the fabric
    total_area = (length1 * width1) + (length2 * width2) + (length3 * width3)
    
    # Finding the height of the flag by dividing the total area by the given length
    height = total_area / 15
    
    result = height
    return result

print(solution())