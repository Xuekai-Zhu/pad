def solution():
    """Sonny received 45 boxes of cookies from his friend yesterday. He gave 12 to his brother, 9 to his sister, and he gave 7 to his cousin. How many boxes of cookies were left for him?"""
    starting_boxes = 45
    given_away_boxes = 12 + 9 + 7
    left_boxes = starting_boxes - given_away_boxes
    result = left_boxes
    return result

print(solution())