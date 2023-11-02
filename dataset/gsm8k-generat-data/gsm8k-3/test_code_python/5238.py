def solution():
    """For every 12 cans you recycle, you receive $0.50, and for every 5 kilograms of newspapers, you receive $1.50. If your family collected 144 cans and 20 kilograms of newspapers, how much money would you receive?"""
    # Define the amount earned per unit
    CAN_PRICE = 0.5
    NEWSPAPER_PRICE = 1.5

    # Calculate the number of units collected
    num_cans = 144
    num_newspapers = 20

    # Calculate the amount earned for the cans and newspapers
    can_earnings = (num_cans // 12) * CAN_PRICE
    newspaper_earnings = (num_newspapers // 5) * NEWSPAPER_PRICE

    # Calculate the total earnings
    total_earnings = can_earnings + newspaper_earnings

    # Display the total earnings
    result = total_earnings
    return result

print(solution())