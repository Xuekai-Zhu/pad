def solution():
    """Five dozens of people are attending your family reunion. Your family was assigned to bring the cans of soda. Each box of soda contains 10 cans and costs $2 per box. It was assumed that each person can consume 2 cans of soda. If you are six in the family and agreed to pay equally for the cost, how much will each of your family members pay?"""
    total_people = 5 * 12
    cans_per_person = 2
    cans_per_box = 10
    boxes_needed = total_people * cans_per_person / cans_per_box
    cost_per_box = 2
    total_cost = boxes_needed * cost_per_box
    num_family_members = 6
    cost_per_member = total_cost / num_family_members
    result = cost_per_member
    return result

print(solution())