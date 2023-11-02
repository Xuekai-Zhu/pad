def solution():
    # Calculate the length of ribbon used to tie one box
    length_per_box = 0.7

    # Calculate the number of boxes Marissa tied with the given length of ribbon
    num_boxes = int((4.5-1) // length_per_box)  # 1 foot of ribbon is left after using 0.7 feet to tie each box

    result = num_boxes
    return result

print(solution())