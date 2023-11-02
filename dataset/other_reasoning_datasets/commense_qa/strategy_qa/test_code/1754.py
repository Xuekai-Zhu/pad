def solution():
    walt_disney_death = "Dec 15, 1966"
    anderson_cooper_birth = "Jun 03, 1967"
    if walt_disney_death < anderson_cooper_birth:
        result = "no"
    else:
        result = "yes"
    return result

print(solution())