def solution():
    john_old_cost = 1200
    apartment_increase = 0.4
    apartment_cost = john_old_cost * (1 + apartment_increase)
    cost_per_person = apartment_cost / 3

    john_savings = john_old_cost - cost_per_person * 12

    result = john_savings
    return result

print(solution())