def solution():
    """Josh gets together with 7 friends. Everyone including him puts 5 dollars into a pot. First place gets 80% of the money. Second and third place split the rest. How much money does third place get?"""
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