def solution():
    # Calculate the amount of the 15% tip
    tip_15_percent = 42

    # Calculate the total bill
    total_bill = (100/115) * tip_15_percent

    # Calculate the amount of the 20% tip
    tip_20_percent = 0.2 * total_bill

    result = tip_20_percent
    return result

print(solution())