def solution():
    """Ali and Ernie lined up boxes to make circles. Ali used 8 boxes to make each of his circles and Ernie used 10 for his. If they had 80 boxes to begin with and Ali makes 5 circles, how many circles can Ernie make?"""
    # Define the number of boxes used to make a circle for Ali and Ernie
    ALI_BOXES = 8
    ERNIE_BOXES = 10

    # Define the total number of boxes and the number of circles Ali makes
    total_boxes = 80
    ali_circles = 5

    # Calculate the number of boxes Ali uses for his circles
    ali_boxes_used = ALI_BOXES * ali_circles

    # Calculate the remaining number of boxes
    remaining_boxes = total_boxes - ali_boxes_used

    # Calculate the number of circles Ernie can make with the remaining boxes
    ernie_circles = remaining_boxes // ERNIE_BOXES

    # Display the number of circles Ernie can make
    result = ernie_circles
    return result

print(solution())