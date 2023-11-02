def solution():
    """Five dozens of people are attending your family reunion. Your family was assigned to bring the cans of soda. Each box of soda contains 10 cans and costs $2 per box. It was assumed that each person can consume 2 cans of soda. If you are six in the family and agreed to pay equally for the cost, how much will each of your family members pay?"""
    # Define the total number of people attending the reunion
    total_people = 60

    # Define the number of cans needed for each person
    cans_per_person = 2

    # Calculate the total number of cans needed
    total_cans = total_people * cans_per_person

    # Define the number of cans per box and the cost per box
    cans_per_box = 10
    cost_per_box = 2

    # Calculate the total number of boxes needed and the total cost
    total_boxes = total_cans // cans_per_box + int(total_cans % cans_per_box != 0)
    total_cost = total_boxes * cost_per_box

    # Calculate the cost per family member
    family_members = 6
    cost_per_member = total_cost / family_members

    result = cost_per_member
    return result

print(solution())