def solution():
    phone_cost = 1300  # cost of the phone
    already_have = 0.4 * phone_cost  # Mike already has 40% of the amount needed
    remaining_cost = phone_cost - already_have  # calculate the remaining amount needed
    result = remaining_cost
    return result

print(solution())