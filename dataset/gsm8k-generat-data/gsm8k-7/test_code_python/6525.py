def solution():
    mom_eyes = 1
    dad_eyes = 3
    num_kids = 3
    kid_eyes = 4

    # Calculate the total number of eyes in the kids
    total_kid_eyes = num_kids * kid_eyes

    # Calculate the total number of eyes in the whole family
    total_eyes = mom_eyes + dad_eyes + total_kid_eyes
    result = total_eyes
    return result

print(solution())