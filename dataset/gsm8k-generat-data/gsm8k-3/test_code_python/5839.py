def solution():
    """Katie's mother wants to get granola bars for all the kids to eat after Katie's soccer game. There will be 30 kids playing soccer, including Katie. Katie's mother wants to get 2 granola bars for each kid, since the bars are not that big and she figures the kids will be very hungry. Each box of granola bars has 12 bars in it. How many boxes should Katie's mother buy?"""
    # Define the number of kids playing soccer and the number of granola bars each kid will get
    num_kids = 30
    num_bars_per_kid = 2

    # Calculate the total number of granola bars needed
    total_bars_needed = num_kids * num_bars_per_kid

    # Calculate the number of boxes Katie's mother should buy
    bars_per_box = 12
    num_boxes = total_bars_needed // bars_per_box
    if total_bars_needed % bars_per_box != 0:
        num_boxes += 1

    # Display the number of boxes Katie's mother should buy
    result = num_boxes
    return result

print(solution())