def solution():
    """A box of ice cream bars costs $7.50 and contains three bars.  6 friends want to each eat 2 bars.  How much money will that require per person?"""
    # Define the cost of a box of ice cream bars and the number of bars per box
    BOX_COST = 7.50
    BARS_PER_BOX = 3

    # Define the number of bars each friend wants to eat
    BARS_PER_FRIEND = 2

    # Define the number of friends
    NUM_FRIENDS = 6

    # Calculate the total number of bars needed
    total_bars = BARS_PER_FRIEND * NUM_FRIENDS

    # Calculate the total number of boxes needed
    total_boxes = total_bars // BARS_PER_BOX + (1 if total_bars % BARS_PER_BOX != 0 else 0)

    # Calculate the cost per person
    cost_per_person = total_boxes * BOX_COST / NUM_FRIENDS / BARS_PER_FRIEND

    # Display the cost per person
    result = cost_per_person
    return result

print(solution())