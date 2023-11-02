def solution():
    """Tom cannot afford a normal doctor, so he goes to a discount clinic that is 70% cheaper. It takes two visits, though, instead of 1. A normal doctor charges $200 for a visit. How much money does he save?"""
    # Define the cost of a normal doctor's visit and the discount percentage
    normal_cost = 200
    discount_percentage = 0.7

    # Calculate the cost of two visits at the discount clinic
    discount_cost = 2 * normal_cost * discount_percentage

    # Calculate the amount saved
    amount_saved = 2 * normal_cost - discount_cost

    # return the result
    result = amount_saved
    return result

print(solution())