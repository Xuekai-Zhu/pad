def solution():
    boxes_ordered = 4  # Farrah ordered 4 boxes
    matchboxes_per_box = 20  # Each box contains 20 matchboxes
    sticks_per_matchbox = 300  # Each matchbox contains 300 match sticks

    # Calculate the total number of match sticks Farrah ordered
    total_sticks_ordered = boxes_ordered * matchboxes_per_box * sticks_per_matchbox
    result = total_sticks_ordered
    return result

print(solution())