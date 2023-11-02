def solution():
    # Calculate the total number of people attending the party
    uncles = 3
    aunts = 4
    cousins = 2 * (uncles + aunts)  # each aunt and uncle has a son and a daughter
    brother = 1
    mother = 1
    total_people = uncles + aunts + cousins + brother + mother
    result = total_people
    return result

print(solution())