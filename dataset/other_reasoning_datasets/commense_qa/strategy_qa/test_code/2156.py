def solution():
    queen_margot_execution_year = 1572
    moliere_birth_year = 1622
    if moliere_birth_year > queen_margot_execution_year:
        result = "no"
    else:
        result = "not enough information"
    return result

print(solution())