def solution():
    """$240 was divided between Kelvin and Samuel. Samuel received 3/4 of the money. From his share, Samuel then spent 1/5 of the original $240 on drinks. How much does Samuel have left?"""
    # Calculate the amount of money Samuel received
    samuel_share = 240 * 3/4

    # Calculate the amount of money Samuel spent on drinks
    drinks_cost = samuel_share * 1/5

    # Calculate the amount of money Samuel has left
    samuel_left = samuel_share - drinks_cost

    result = samuel_left
    return result

print(solution())