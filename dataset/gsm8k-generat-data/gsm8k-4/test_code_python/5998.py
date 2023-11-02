def solution():
    """Ali and Ernie lined up boxes to make circles. Ali used 8 boxes to make each of his circles and Ernie used 10 for his. If they had 80 boxes to begin with and Ali makes 5 circles, how many circles can Ernie make?"""
    # Define the number of boxes Ali used per circle and Ernie used per circle
    ALI_BOXES_PER_CIRCLE = 8
    ERNIE_BOXES_PER_CIRCLE = 10

    # Define the total number of boxes they had to begin with
    TOTAL_BOXES = 80

    # Calculate the number of circles Ali made
    ali_circles = 5
    
    # Calculate the remaining boxes after Ali made his circles
    remaining_boxes = TOTAL_BOXES - (ali_circles * ALI_BOXES_PER_CIRCLE)

    # Calculate the number of circles Ernie can make with the remaining boxes
    ernie_circles = remaining_boxes // ERNIE_BOXES_PER_CIRCLE

    result = ernie_circles
    return result

print(solution())