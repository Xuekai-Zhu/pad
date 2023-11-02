def solution():
    # Calculate the number of buttons Mark has after Shane gives him 3 times the initial amount
    new_buttons = 14 + (3 * 14)  # Shane gave Mark 3 times the initial amount of buttons
    # Calculate the number of buttons Mark has after Sam takes half of them
    end_buttons = new_buttons / 2  # Sam takes half of Mark's buttons
    result = end_buttons
    return result

print(solution())