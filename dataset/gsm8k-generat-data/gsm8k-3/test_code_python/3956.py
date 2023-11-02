def solution():
    """Five dozens of people are attending your family reunion. Your family was assigned to bring the cans of soda. Each box of soda contains 10 cans and costs $2 per box. It was assumed that each person can consume 2 cans of soda. If you are six in the family and agreed to pay equally for the cost, how much will each of your family members pay?"""
    # Calculate the total number of people attending the reunion
    total_people = 5 * 12

    # Calculate the total number of cans needed
    total_cans = total_people * 2

    # Calculate the number of boxes needed
    boxes_needed = total_cans // 10
    if total_cans % 10 != 0:
        boxes_needed += 1

    # Calculate the total cost of the soda
    total_cost = boxes_needed * 2

    # Calculate the cost per family member
    cost_per_person = total_cost / 6

    # Display the cost per person
    result = cost_per_person
    return result

print(solution())