def solution():
    total_number_of_pens = 20 * 5
    pens_given_to_friends = 0.4 * total_number_of_pens
    pens_given_to_classmates = 0.25 * (total_number_of_pens - pens_given_to_friends)
    pens_left_for_lenny = total_number_of_pens - pens_given_to_friends - pens_given_to_classmates
    result = pens_left_for_lenny
    return result

print(solution())