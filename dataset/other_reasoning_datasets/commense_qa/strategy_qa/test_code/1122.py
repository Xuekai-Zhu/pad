def solution():
    jainism_start_year = 500
    plato_birth_year = 428
    belief_in_karma_reincarnation = True
    if plato_birth_year < jainism_start_year and belief_in_karma_reincarnation:
        result = "yes"
    else:
        result = "no"
    return result

print(solution())