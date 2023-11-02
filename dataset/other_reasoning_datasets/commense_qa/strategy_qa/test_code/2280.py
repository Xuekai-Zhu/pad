def solution():
    queen_victoria_death_year = 1901
    elizabeth_ii_birth_year = 1926
    if elizabeth_ii_birth_year > queen_victoria_death_year:
        result = "no"
    else:
        result = "yes"
    return result

print(solution())