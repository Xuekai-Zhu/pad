def solution():
    total_employees = 180
    # Let's assume x is the number of women
    x = (total_employees + 20) / 2
    # The number of men is 20 less than the number of women
    men = x - 20
    result = men
    return result

print(solution())