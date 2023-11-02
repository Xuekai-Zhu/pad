def solution():
    num_boxes = 400
    food_value_per_box = 80
    additional_supplies_value_per_box = 165

    # Calculate the total cost of all initial boxes of food and supplies
    total_initial_cost = num_boxes * (food_value_per_box + additional_supplies_value_per_box)

    # Calculate the amount of money the organization received from the anonymous donor
    additional_funding = 4 * total_initial_cost

    # Calculate the new total cost of all boxes of food and supplies
    new_total_cost = total_initial_cost + additional_funding

    # Calculate the new total number of boxes that can be packed
    new_total_boxes = new_total_cost / (food_value_per_box + additional_supplies_value_per_box)
    result = new_total_boxes
    return result

print(solution())