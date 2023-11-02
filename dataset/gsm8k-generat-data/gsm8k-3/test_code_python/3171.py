def solution():
    """Brian is taping up some boxes. Each box needs three pieces of tape, one as long as the long side and two as long as the short side. If Brian tapes up 5 boxes that measure 15 inches by 30 inches and 2 boxes that measure 40 inches square, how much tape does he need?"""
    # Define the dimensions of the boxes
    box1_length = 15
    box1_width = 30
    box2_length = 40
    box2_width = 40

    # Calculate the amount of tape needed for each box
    box1_tape = box1_length + 2 * box1_width
    box2_tape = 2 * box2_length + 4 * box2_width

    # Calculate the total amount of tape needed
    total_tape = 5 * box1_tape + 2 * box2_tape

    # Display the total amount of tape needed
    result = total_tape
    return result

print(solution())