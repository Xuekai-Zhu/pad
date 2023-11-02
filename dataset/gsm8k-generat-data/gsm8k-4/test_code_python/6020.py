def solution():
    """Carrie buys 4 shirts, 2 pairs of pants, and 2 jackets. Each shirt costs $8. Each pair of pants costs $18. Each jacket costs $60. If Carrie’s mom pays for half of the total cost of all the clothes, how much does Carrie pay for the clothes?"""
    # Calculate the total cost of the clothes
    total_cost = (4 * 8) + (2 * 18) + (2 * 60)

    # Calculate the amount Carrie's mom pays
    mom_pays = total_cost / 2

    # Calculate the amount Carrie pays
    carrie_pays = total_cost - mom_pays

    # Return the result
    result = carrie_pays
    return result

print(solution())