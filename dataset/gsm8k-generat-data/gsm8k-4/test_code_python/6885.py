def solution():
    """Farrah ordered 4 boxes from Amazon containing 20 matchboxes each. If each matchbox has 300 sticks, calculate the total number of match sticks that Farah ordered?"""
    # Define the number of boxes and matchboxes
    boxes = 4
    matchboxes_per_box = 20

    # Define the number of match sticks per matchbox
    matchsticks_per_matchbox = 300

    # Calculate the total number of match sticks
    total_matchsticks = boxes * matchboxes_per_box * matchsticks_per_matchbox

    # Display the result
    result = total_matchsticks
    return result

print(solution())