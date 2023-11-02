def solution():
    # Find Phoebe's current age
    phoebe_age_in_5_years = (25 + 5) / 3
    phoebe_current_age = phoebe_age_in_5_years - 5

    # Find Jacob's current age
    jacob_current_age = (3/5) * phoebe_current_age
    result = jacob_current_age
    return result

print(solution())