def solution():
    """A box of ice cream bars costs $7.50 and contains three bars. 6 friends want to each eat 2 bars. How much money will that require per person?"""
    # Define the cost of a box of ice cream bars and the number of bars per box
    box_cost = 7.50
    bars_per_box = 3

    # Calculate the total number of bars needed for 6 friends to each have 2 bars
    total_bars_needed = 6 * 2

    # Calculate the total number of boxes needed to have enough bars
    total_boxes_needed = total_bars_needed / bars_per_box

    # Calculate the cost per person
    cost_per_person = total_boxes_needed * box_cost / 6

    result = cost_per_person
    return result

print(solution())