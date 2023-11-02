def solution():
    """In five years, Rehana will be three times as old as Phoebe. If Rehana is currently 25 years old, and Jacob, Rehana's brother, is 3/5 of Phoebe's current age, how old is Jacob now?"""
    # Define Rehana's current age and the age ratio between her and Phoebe
    rehana_age = 25
    rehana_phoebe_ratio = 3

    # Calculate Phoebe's current age
    phoebe_age = (rehana_age - 5) / rehana_phoebe_ratio

    # Calculate Jacob's age, which is 3/5 of Phoebe's current age
    jacob_age = phoebe_age * 3/5
    result = jacob_age
    return result

print(solution())