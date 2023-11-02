def solution():
    coen_brothers_birth_years = [1954, 1957]
    brothers_grimm_death_years = [1859, 1863]
    if any(year in coen_brothers_birth_years for year in brothers_grimm_death_years):
        result = "no"
    else:
        result = "yes"
    return result

print(solution())