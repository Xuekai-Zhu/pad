def solution():
    """Marissa has 4.5 feet of ribbon that she wants to use to tie some boxes. If 1 foot of ribbon is left after Marissa uses 0.7 feet of ribbon to tie each box, find out how many boxes she tied?"""
    # Define the length of ribbon used per box
    RIBBON_PER_BOX = 0.7

    # Define the total length of ribbon Marissa has
    total_ribbon = 4.5

    # Calculate the number of boxes Marissa can tie
    boxes = (total_ribbon - 1) / RIBBON_PER_BOX

    # Display the number of boxes
    result = boxes
    return result

print(solution())