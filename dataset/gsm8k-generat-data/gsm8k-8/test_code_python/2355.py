def solution():
    # Define the amount of tape required for each box
    large_box_tape = 4 + 1
    medium_box_tape = 2 + 1
    small_box_tape = 1 + 1

    # Calculate the total amount of tape used for each box type
    total_large_tape = large_box_tape * 2
    total_medium_tape = medium_box_tape * 8
    total_small_tape = small_box_tape * 5

    # Calculate the total amount of tape used
    total_tape_used = total_large_tape + total_medium_tape + total_small_tape

    result = total_tape_used
    return result

print(solution())