def solution():
    black_people_considered_human = False
    slavery_benefited_black_slaves = True
    writers_considered_all_humans = True

    if not black_people_considered_human and slavery_benefited_black_slaves and writers_considered_all_humans:
        result = "yes"
    else:
        result = "no"
    return result

print(solution())