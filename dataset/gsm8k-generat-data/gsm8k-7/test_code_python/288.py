def solution():
    cheap_membership_cost = 10 * 12 + 50
    expensive_membership_cost = 3 * cheap_membership_cost
    expensive_membership_sign_up_fee = 4 * expensive_membership_cost

    total_cost = cheap_membership_cost + expensive_membership_sign_up_fee

    result = total_cost
    return result

print(solution())