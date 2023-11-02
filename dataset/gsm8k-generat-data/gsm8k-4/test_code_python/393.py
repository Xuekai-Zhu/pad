def solution():
    """Josh built his little brother a rectangular sandbox. The perimeter of the sandbox is 30 feet and the length is twice the width. What is the width of the sandbox?"""
    # let w is the width, then the length is 2w
    # calculate the perimeter P: P=2(l+w)
    
    # Define the perimeter of the sandbox
    perimeter = 30

    # Define the width of the sandbox
    width = None

    # Define the length of the sandbox
    length = 2 * width

    # Solve for the width using the equation 2(l+w)=P
    width = (perimeter - length) / 2

    result = width
    return result

print(solution())