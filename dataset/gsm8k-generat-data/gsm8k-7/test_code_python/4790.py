def solution():
    rehana_current_age = 25
    phoebe_future_age = 3 * (rehana_current_age + 5)

    # Calculate Phoebe's current age
    phoebe_current_age = phoebe_future_age - 5

    # Calculate Jacob's current age
    jacob_current_age = (3/5) * phoebe_current_age
    result = jacob_current_age
    return result

print(solution())