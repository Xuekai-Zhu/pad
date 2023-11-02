def solution():
    """Jason has three times as many toys as John. If John has 6 more toys than Rachel and Rachel has 1 toy, how many toys does Jason have?"""
    # Define the number of toys Rachel has
    rachel_toys = 1

    # Calculate the number of toys John has
    john_toys = rachel_toys + 6

    # Calculate the number of toys Jason has
    jason_toys = john_toys * 3

    # Display the number of toys Jason has
    result = jason_toys
    return result

print(solution())