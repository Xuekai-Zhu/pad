def solution():
    """In five years, Rehana will be three times as old as Phoebe. If Rehana is currently 25 years old, and Jacob, Rehana's brother, is 3/5 of Phoebe's current age, how old is Jacob now?"""
    rehana_age = 25
    phoebe_age_in_5_years = (rehana_age + 5) / 3
    phoebe_age_now = phoebe_age_in_5_years - 5
    jacob_age = (3/5) * phoebe_age_now
    result = jacob_age
    return result

print(solution())