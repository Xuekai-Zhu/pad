def solution():
    # Calculate the amount of tax on the check
    tax = 0.2 * 15

    # Calculate the total amount of the bill including tax
    total_bill = 15 + tax

    # Calculate Jason's tip
    tip = 20 - total_bill

    result = tip
    return result

print(solution())