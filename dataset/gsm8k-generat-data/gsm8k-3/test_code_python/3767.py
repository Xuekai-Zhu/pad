def solution():
    """In a basketball game, Jon scored 3 points. Jack scored 5 points more than Jon, and Tom scored 4 less than the points of Jon and Jack together. How many points did they score altogether?"""
    # Define Jon's score
    jon_score = 3

    # Define Jack's score
    jack_score = jon_score + 5

    # Define Tom's score
    tom_score = jon_score + jack_score - 4

    # Calculate the total score
    total_score = jon_score + jack_score + tom_score

    # Display the total score
    result = total_score
    return result

print(solution())