def solution():
    darpa_founded_year = 1958
    einstein_death_year = 1955
    if darpa_founded_year > einstein_death_year:
        result = "no"
    else:
        result = "unknown"
    return result

print(solution())