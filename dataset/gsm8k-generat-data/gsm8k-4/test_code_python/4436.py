def solution():
    """Mike wants to buy a new phone. The cost of the phone is $1300. How much more money does Mike need if he already has 40% of the amount he needs?"""
    # Define the cost of the phone and the amount Mike already has
    phone_cost = 1300
    amount_already_has = phone_cost * 0.4

    # Calculate the amount Mike still needs to save
    amount_still_needs = phone_cost - amount_already_has

    # return the result
    result = amount_still_needs
    return result

print(solution())