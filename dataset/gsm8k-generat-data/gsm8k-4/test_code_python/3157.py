def solution():
    """Chris’s internet bill is $45 per month for 100 GB and $0.25 for every 1 GB over. His bill for this month is $65. How many GB over was Chris charged for on this bill?"""
    # Define the base cost and the cost per extra GB
    BASE_COST = 45
    EXTRA_COST = 0.25

    # Define the total bill for this month
    total_bill = 65

    # Calculate the GB used in excess of the base amount
    excess_GB = (total_bill - BASE_COST) / EXTRA_COST

    result = excess_GB
    return result

print(solution())