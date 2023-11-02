def solution():
    """Tyrone empties his piggy bank and finds two $1 bills, a $5 bill, 13 quarters, 20 dimes, 8 nickels, and 35 pennies. How much money does Tyrone have?"""
    total = 2*1 + 1*5 + 0.25*13 + 0.10*20 + 0.05*8 + 0.01*35
    result = "${:.2f}".format(total)
    return result

print(solution())