def solution():
    num_uncles = 3
    num_aunts = 4
    num_cousins = (num_aunts * 2)
    num_other_family = 2  # brother and mother

    # Calculate the total number of people coming to the party
    total_people = num_uncles + num_aunts + num_cousins + num_other_family
    result = total_people
    return result

print(solution())