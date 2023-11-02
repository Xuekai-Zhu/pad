def solution():
    # Calculate the net change in the number of lions per month
    net_change = 5 - 1  # lion cubs born at the rate of 5 per month and lions die at the rate of 1 per month

    # Calculate the total number of lions after 1 year
    total_lions = 100 + (net_change * 12)  # 1 year = 12 months
    result = total_lions
    return result

print(solution())