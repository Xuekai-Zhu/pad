def solution():
    """A computer factory produces 1500 computers per day. They sell each computer for $150. If they sold 1 week's worth of production, how much money will the company earn?"""
    # Define the number of computers produced per day and their selling price
    COMPUTERS_PER_DAY = 1500
    PRICE_PER_COMPUTER = 150

    # Calculate the number of computers produced in a week
    computers_per_week = COMPUTERS_PER_DAY * 7

    # Calculate the total earnings in a week
    total_earnings = computers_per_week * PRICE_PER_COMPUTER

    # Display the total earnings
    result = total_earnings
    return result

print(solution())