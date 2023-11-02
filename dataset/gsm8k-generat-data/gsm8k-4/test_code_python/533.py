def solution():
    """There were 100 jelly beans in a bag to be given away on Halloween. Out of the 40 children taking part in the Halloween celebration, 80% were allowed to draw jelly beans from the bag. Each child drew two jelly beans out of the bag. How many jelly beans remained in the bag after the children took their share?"""
    # Define the initial number of jelly beans
    initial_jelly_beans = 100

    # Calculate the number of children allowed to draw jelly beans
    allowed_children = 40 * 0.8

    # Calculate the total number of jelly beans drawn
    total_jelly_beans = allowed_children * 2

    # Calculate the number of jelly beans remaining in the bag
    remaining_jelly_beans = initial_jelly_beans - total_jelly_beans

    result = remaining_jelly_beans
    return result

print(solution())