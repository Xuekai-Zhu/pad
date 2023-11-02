def solution():
    """Paul earns $12.50 for each hour that he works. He then has to pay 20% for taxes and fees. After working 40 hours, Paul receives his paycheck. If he spends 15% of his paycheck on gummy bears, how much, in dollars, does he have left?"""
    # Calculate the gross earnings
    gross_pay = 40 * 12.50

    # Calculate the amount of taxes and fees
    taxes_and_fees = gross_pay * 0.20

    # Calculate the net pay
    net_pay = gross_pay - taxes_and_fees

    # Calculate the amount spent on gummy bears
    gummy_bears = net_pay * 0.15

    # Calculate the amount left after buying gummy bears
    left = net_pay - gummy_bears

    # Display the amount left
    result = left
    return result

print(solution())