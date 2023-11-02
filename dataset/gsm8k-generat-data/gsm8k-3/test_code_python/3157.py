def solution():
    """Chris’s internet bill is $45 per month for 100 GB and $0.25 for every 1 GB over. His bill for this month is $65. How many GB over was Chris charged for on this bill?"""
    # Define the base cost and overage rate
    BASE_COST = 45
    OVERAGE_RATE = 0.25

    # Calculate the amount of overage
    overage = (65 - 45) / OVERAGE_RATE

    # Subtract the base amount to get the overage amount
    overage_amount = overage - 100

    # Display the overage amount
    result = overage_amount
    return result

print(solution())