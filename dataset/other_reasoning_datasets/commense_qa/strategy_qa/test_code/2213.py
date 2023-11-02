def solution():
    current_year = 2021
    debut_year = 1995
    years_since_debut = current_year - debut_year
    if years_since_debut <= 0:
        result = "yes"
    else:
        result = "no"
    return result

print(solution())