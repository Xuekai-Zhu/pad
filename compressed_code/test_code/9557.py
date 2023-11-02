def solution():
    
    rehana_age = 25
    phoebe_age_in_5_years = (rehana_age + 5) / 3
    phoebe_age_now = phoebe_age_in_5_years - 5
    jacob_age = (3/5) * phoebe_age_now
    result = jacob_age
    return result

print(solution())