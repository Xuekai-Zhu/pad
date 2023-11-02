def solution():
    census_interval = 10
    initial_census_year = 2020
    next_census_year = initial_census_year + census_interval
    anchovy_lifespan = 5
    anchovy_birth_year = 2020
    
    if next_census_year - anchovy_birth_year <= anchovy_lifespan:
        result = "yes"
    else:
        result = "no"
    return result

print(solution())