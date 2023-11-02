def solution():
    rehana_current_age = 25  # given
    phoebe_current_age = (rehana_current_age + 5) / 3  # Rehana will be three times as old as Phoebe in five years
    jacob_age_ratio = 3 / 5
    jacob_current_age = jacob_age_ratio * phoebe_current_age  # Jacob's age is 3/5 of Phoebe's current age

    result = jacob_current_age
    return result

print(solution())