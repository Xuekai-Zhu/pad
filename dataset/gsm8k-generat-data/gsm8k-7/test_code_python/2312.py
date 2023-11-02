def solution():
    savings = 1200
    mother_contribution = 3/5 * savings
    brother_contribution = 2 * mother_contribution
    total_money = savings + mother_contribution + brother_contribution - 400
    result = total_money
    return result

print(solution())