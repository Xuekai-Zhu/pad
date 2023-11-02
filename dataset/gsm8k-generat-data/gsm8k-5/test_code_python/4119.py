def solution():
    # Calculate Grant's earnings for each month
    month1 = 350
    month2 = (2*month1) + 50
    month3 = 4*(month1+month2)

    # Calculate Grant's total earnings for the three months
    total_earnings = month1 + month2 + month3
    result = total_earnings
    return result

print(solution())