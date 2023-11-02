def solution():
    """Marissa has 4.5 feet of ribbon that she wants to use to tie some boxes. If 1 foot of ribbon is left after Marissa uses 0.7 feet of ribbon to tie each box, find out how many boxes she tied?"""
    # Define the total length of ribbon and the length of ribbon used to tie each box
    total_length = 4.5
    length_per_box = 0.7

    # Calculate the number of boxes that can be tied with the given length of ribbon
    boxes = (total_length - 1) / length_per_box

    result = round(boxes)
    return result

print(solution())