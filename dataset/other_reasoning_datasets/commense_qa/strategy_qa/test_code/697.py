def solution():
    sweden_part_of_scandinavia = True
    riksdag_legislative_branch = True
    if sweden_part_of_scandinavia and riksdag_legislative_branch:
        result = "yes"
    else:
        result = "no"
    return result

print(solution())