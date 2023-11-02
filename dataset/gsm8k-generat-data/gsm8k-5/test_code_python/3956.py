def solution():
    total_people = 5 * 12  # Five dozens of people are attending, which is equal to 5*12=60 people
    cans_per_person = 2  # Each person can consume 2 cans of soda
    total_cans = total_people * cans_per_person  # Calculate the total number of cans needed
    cans_per_box = 10  # Each box of soda contains 10 cans
    boxes_needed = total_cans // cans_per_box + 1  # Calculate the number of boxes needed, rounding up to the nearest box
    cost_per_box = 2  # Each box of soda costs $2
    total_cost = boxes_needed * cost_per_box  # Calculate the total cost of the soda

    family_size = 6  # There are six people in the family
    cost_per_person = total_cost / family_size  # Divide the total cost equally among family members
    result = cost_per_person
    return result

print(solution())