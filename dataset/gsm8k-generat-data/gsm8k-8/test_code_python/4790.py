def solution():
    # Define Rehana's current age
    rehana_current_age = 25

    # Calculate Phoebe's current age
    phoebe_current_age = (rehana_current_age - 5) / 3

    # Calculate Jacob's current age
    jacob_current_age = 0.6 * phoebe_current_age

    result = jacob_current_age
    return result

print(solution())