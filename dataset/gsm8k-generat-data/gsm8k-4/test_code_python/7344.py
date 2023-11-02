def solution():
    """The cheerleading coach is ordering new uniforms. There are 4 cheerleaders who need a size 2, a certain number who need a size 6, and half that number who need a size 12. If there are 19 cheerleaders total, how many cheerleaders need a size 6?"""
    # Define the number of cheerleaders who need size 2
    size_2 = 4

    # Calculate the number of cheerleaders who need size 12
    size_12 = (19 - size_2) / 3

    # Calculate the number of cheerleaders who need size 6
    size_6 = 19 - size_2 - size_12

    # Return the result
    result = size_6
    return result

print(solution())