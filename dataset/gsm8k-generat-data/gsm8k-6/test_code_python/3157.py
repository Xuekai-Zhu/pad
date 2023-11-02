def solution():
    # Calculate the amount of GB used
    base_GBs = 100
    excess_bill = 65 - 45  # difference between the total bill and the base bill
    excess_GBs = excess_bill / 0.25  # calculate the number of GBs charged for
    total_GBs = base_GBs + excess_GBs  # calculate the total GB used
    over_GBs = total_GBs - base_GBs  # calculate the GBs charged for over the base amount
    result = over_GBs
    return result

print(solution())