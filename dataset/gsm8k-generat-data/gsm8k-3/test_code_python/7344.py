def solution():
    """The cheerleading coach is ordering new uniforms. There are 4 cheerleaders who need a size 2, a certain number who need a size 6, and half that number who need a size 12. If there are 19 cheerleaders total, how many cheerleaders need a size 6?"""
    # Define the number of cheerleaders who need a size 2
    size_2 = 4

    # Define the total number of cheerleaders who need a size 6 and 12
    size_6_and_12 = 19 - size_2

    # Define the number of cheerleaders who need a size 12
    size_12 = size_6_and_12 / 2

    # Calculate the number of cheerleaders who need a size 6
    size_6 = size_6_and_12 - size_12

    # Display the number of cheerleaders who need a size 6
    result = size_6
    return result

print(solution())