def solution():
    # Initialize variables
    savings = 2+4+8
    next_month_savings = 16

    # Loop through the remaining months
    for i in range(3, 6):
        savings += next_month_savings
        next_month_savings *= 2

    result = savings
    return result

print(solution())