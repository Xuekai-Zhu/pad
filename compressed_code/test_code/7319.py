def solution():
    
    num_friends = 8
    amount_per_person = 5
    total_pot = num_friends * amount_per_person
    first_place = total_pot * 0.8
    remaining_pot = total_pot - first_place
    second_third_split = remaining_pot / 2
    third_place = second_third_split
    result = third_place
    return result

print(solution())