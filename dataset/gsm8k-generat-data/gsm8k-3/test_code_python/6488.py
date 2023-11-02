def solution():
    """A charity organization's goal is to distribute 400 boxes of food to a community that was recently destroyed by a flood. Each box contains $80 worth of food and $165 worth of additional supplies such as toiletries and fresh linens. Then, an anonymous donor gives the organization 4 times the amount of money they had already spent, allowing them to pack many more boxes. How many boxes do they pack in total?"""
    # Define the number of food boxes and the cost of supplies per box
    NUM_BOXES = 400
    SUPPLIES_COST_PER_BOX = 165

    # Calculate the total cost of supplies for the original goal of 400 boxes
    original_supplies_cost = NUM_BOXES * SUPPLIES_COST_PER_BOX

    # Calculate the total cost of the original goal of 400 boxes
    original_total_cost = NUM_BOXES * (80 + SUPPLIES_COST_PER_BOX)

    # Calculate the amount of money the donor gives the organization
    donor_money = original_total_cost * 4 - original_total_cost

    # Calculate the new number of boxes the organization can pack with the donor's money
    new_num_boxes = int(donor_money / (80 + SUPPLIES_COST_PER_BOX))

    # Calculate the total number of boxes the organization can pack
    total_num_boxes = NUM_BOXES + new_num_boxes

    # Display the total number of boxes the organization can pack
    result = total_num_boxes
    return result

print(solution())