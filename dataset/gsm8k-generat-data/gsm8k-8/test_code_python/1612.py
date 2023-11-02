def solution():
    # Calculate Paul's earnings before taxes and fees
    earnings = 12.50 * 40

    # Calculate the amount of taxes and fees he needs to pay
    taxes_and_fees = 0.2 * earnings

    # Calculate Paul's net earnings after taxes and fees
    net_earnings = earnings - taxes_and_fees

    # Calculate the amount he spends on gummy bears
    gummy_bears = 0.15 * net_earnings

    # Calculate how much he has left
    left_over = net_earnings - gummy_bears
    result = left_over
    return result

print(solution())