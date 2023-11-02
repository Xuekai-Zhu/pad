def solution():
    # Calculate the total number of eyes for the mom and dad
    mom_eyes = 1
    dad_eyes = 3
    total_parents_eyes = mom_eyes + dad_eyes

    # Calculate the total number of eyes for the kids
    num_kids = 3
    kid_eyes_each = 4
    total_kids_eyes = num_kids * kid_eyes_each

    # Calculate the total number of eyes for the whole family
    total_eyes = total_parents_eyes + total_kids_eyes
    result = total_eyes
    return result

print(solution())