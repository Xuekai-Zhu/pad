def solution():
    president_of_mexico_is_a_citizen = True
    voter_must_be_us_citizen = True
    if president_of_mexico_is_a_citizen and not voter_must_be_us_citizen:
        result = "yes"
    else:
        result = "no"
    return result

print(solution())