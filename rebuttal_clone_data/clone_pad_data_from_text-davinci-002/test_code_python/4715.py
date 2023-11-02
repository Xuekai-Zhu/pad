def solution():
    regular_charge = (10 * 2) + (5 * 1)
    discount = regular_charge * 0.18
    fine = 20
    total_charge = regular_charge - discount + fine
    result = total_charge
    return result

print(solution())