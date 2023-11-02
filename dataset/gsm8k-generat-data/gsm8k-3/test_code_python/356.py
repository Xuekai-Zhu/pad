def solution():
    """Seth bought some boxes of oranges. He gave a box to his mother. He then gave away half of the remaining boxes. If Seth has 4 boxes of oranges left, how many boxes did he buy in the first place?"""
    # We can work backwards from the 4 boxes remaining
    # If Seth has 4 boxes remaining after giving away half of the remaining boxes, he must have started with 8 boxes
    # If he gave away half of the remaining boxes before that, he would have had 16 boxes
    # If he gave a box to his mother before that, he would have started with 17 boxes

    # Display the number of boxes Seth bought in the first place
    result = 17
    return result

print(solution())