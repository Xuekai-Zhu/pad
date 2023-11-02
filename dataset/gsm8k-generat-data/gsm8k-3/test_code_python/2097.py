def solution():
    """Ali, Nada, and John have a total of $67 in their wallets. Ali has $5 less than Nada and John has 4 times more than Nada. How much money does John have?"""
    # Let's define the variables
    j = 0
    n = 0
    a = 0

    # Let's define the equations
    # The sum of Ali, Nada, and John's money is $67
    # Ali has $5 less than Nada
    # John has 4 times more than Nada

    n = (67 + 5) / (1 + 1 + 4)
    a = n - 5
    j = n * 4

    # Let's calculate John's money
    result = j
    return result

print(solution())