def solution():
    num_people = 5 * 12
    cans_per_box = 10
    cost_per_box = 2.0
    cans_per_person = 2
    num_family_members = 6

    # Calculate the total number of cans of soda needed
    total_cans = num_people * cans_per_person

    # Calculate the total number of boxes of soda needed
    total_boxes = total_cans / cans_per_box

    # Calculate the total cost of all boxes of soda
    total_cost = total_boxes * cost_per_box

    # Calculate the cost per family member
    cost_per_family_member = total_cost / num_family_members
    result = cost_per_family_member
    return result

print(solution())