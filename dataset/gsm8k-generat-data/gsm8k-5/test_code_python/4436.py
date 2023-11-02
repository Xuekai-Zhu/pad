def solution():
    phone_cost = 1300  # The cost of the phone is $1300
    already_have = 0.4 * phone_cost  # Mike already has 40% of the phone cost

    # Calculate how much money Mike still needs to buy the phone
    remaining_cost = phone_cost - already_have
    result = remaining_cost
    return result

print(solution())