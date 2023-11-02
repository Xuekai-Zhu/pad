def solution():
    is_human = True
    is_cow = False
    can_only_humans_produce_human_offspring = True
    if not is_human and is_cow and not can_only_humans_produce_human_offspring:
        result = "yes"
    else:
        result = "no"
    return result

print(solution())