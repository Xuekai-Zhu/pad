def solution():
    """There are 160 tissues inside a tissue box.   If Tucker bought 3 boxes, and used 210 tissues while he was sick with the flu, how many tissues would he have left?"""
    # Define the number of tissues in each box and the number of boxes purchased
    TISSUES_PER_BOX = 160
    NUM_BOXES_PURCHASED = 3

    # Calculate the total number of tissues purchased
    total_tissues = TISSUES_PER_BOX * NUM_BOXES_PURCHASED

    # Calculate the number of tissues used
    tissues_used = 210

    # Calculate the number of tissues remaining
    tissues_remaining = total_tissues - tissues_used

    # Display the number of tissues remaining
    result = tissues_remaining
    return result

print(solution())