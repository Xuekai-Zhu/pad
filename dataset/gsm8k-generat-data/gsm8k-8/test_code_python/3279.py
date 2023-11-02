def solution():
    # Define the number of kids and whiteboards
    num_kids = 4
    num_whiteboards = 3

    # Calculate the time it takes for four kids to wash one whiteboard
    time_per_whiteboard = 20 / (num_kids * num_whiteboards)

    # Calculate the time it takes for one kid to wash one whiteboard
    time_per_whiteboard_per_kid = time_per_whiteboard * num_kids

    # Calculate the time it takes for one kid to wash six whiteboards
    total_time = time_per_whiteboard_per_kid * 6
    result = total_time
    return result

print(solution())