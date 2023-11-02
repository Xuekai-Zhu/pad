def solution():
    """There were 100 jelly beans in a bag to be given away on Halloween. Out of the 40 children taking part in the Halloween celebration, 80% were allowed to draw jelly beans from the bag. Each child drew two jelly beans out of the bag. How many jelly beans remained in the bag after the children took their share?"""
    # Define the number of jelly beans in the bag
    jelly_beans = 100

    # Calculate the number of children who were allowed to draw from the bag
    num_children = 40
    allowed_children = int(num_children * 0.8)

    # Calculate the number of jelly beans drawn from the bag
    num_jelly_beans_drawn = allowed_children * 2

    # Calculate the number of jelly beans remaining in the bag
    jelly_beans_remaining = jelly_beans - num_jelly_beans_drawn

    # Display the number of jelly beans remaining in the bag
    result = jelly_beans_remaining
    return result

print(solution())