def solution():
    """Ali and Ernie lined up boxes to make circles. Ali used 8 boxes to make each of his circles and Ernie used 10 for his. If they had 80 boxes to begin with and Ali makes 5 circles, how many circles can Ernie make?"""
    total_boxes = 80
    ali_circles = 5
    ali_boxes_used = ali_circles * 8
    remaining_boxes = total_boxes - ali_boxes_used
    ernie_circles = remaining_boxes // 10
    result = ernie_circles
    return result

print(solution())