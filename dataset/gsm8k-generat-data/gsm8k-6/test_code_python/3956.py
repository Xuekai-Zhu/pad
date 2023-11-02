def solution():
    num_people = 5 * 12  # 5 dozens of people attending
    num_cans = num_people * 2  # each person can consume 2 cans of soda
    num_boxes = num_cans / 10  # each box contains 10 cans
    cost_per_box = 2  # cost of each box of soda
    total_cost = num_boxes * cost_per_box  # total cost of all the boxes of soda
    num_family_members = 6  # number of people in the family
    cost_per_person = total_cost / num_family_members  # cost each family member has to pay
    result = cost_per_person
    return result

print(solution())