def solution():
    # Number of uncles and aunts
    num_uncles = 3
    num_aunts = 4

    # Number of cousins (sons and daughters of uncles and aunts)
    num_cousins = (num_uncles + num_aunts) * 2

    # Number of immediate family members
    num_immediate_family = 1 + 1

    # Total number of people coming to the party
    total_people = num_uncles + num_aunts + num_cousins + num_immediate_family
    result = total_people
    return result

print(solution())