def solution():
    """Mike wants to buy a new phone. The cost of the phone is $1300. How much more money does Mike need if he already has 40% of the amount he needs?"""
    phone_cost = 1300
    already_has = 0.4 * phone_cost
    remaining_cost = phone_cost - already_has
    result = remaining_cost
    return result

print(solution())