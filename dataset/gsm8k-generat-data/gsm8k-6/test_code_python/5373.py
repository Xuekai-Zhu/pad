def solution():
    # Calculate the amount of money Jim has for retirement
    retirement = 0.25 * 1120

    # Calculate the amount of money Jim has after taxes and retirement
    net_pay = 1120 - retirement - 100

    result = net_pay
    return result

print(solution())