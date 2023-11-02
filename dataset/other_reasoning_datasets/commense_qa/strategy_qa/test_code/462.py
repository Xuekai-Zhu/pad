def solution():
    elijah_cummings_death_date = "October 17th, 2019"
    presidential_election_year = 2020
    if presidential_election_year > int(elijah_cummings_death_date[-4:]):
        result = "no"
    else:
        result = "not applicable"
    return result

print(solution())