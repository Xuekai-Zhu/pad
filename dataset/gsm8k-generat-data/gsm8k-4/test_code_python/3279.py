def solution():
    """Four kids can wash three whiteboards in 20 minutes. How long would it take, in minutes, for one kid to wash six whiteboards?"""
    # Define the number of kids, whiteboards, and time to wash
    num_kids = 4
    num_whiteboards = 3
    time_to_wash = 20

    # Calculate the time it takes for one kid to wash one whiteboard
    one_kid_one_whiteboard = time_to_wash / (num_kids * num_whiteboards)

    # Calculate the time it takes for one kid to wash six whiteboards
    one_kid_six_whiteboards = one_kid_one_whiteboard * 6

    # return the result
    result = one_kid_six_whiteboards
    return result

print(solution())