def solution():
    """Tom decides to lease a car.  He drives 50 miles on Monday, Wednesday, and Friday, and Sunday for the rest of the days he drives 100 miles.  He has to pay $.1 per mile he drives.  He also has to pay a weekly fee of $100.  How much does he have to pay in a year."""
    # Define the daily and weekly number of miles Tom drives
    MON_WED_FRI_MILES = 50
    SUN_MILES = 100
    OTHER_MILES = SUN_MILES

    # Define the price per mile and weekly fee
    PRICE_PER_MILE = 0.1
    WEEKLY_FEE = 100

    # Calculate the yearly number of miles driven
    yearly_miles = (MON_WED_FRI_MILES * 3) + (OTHER_MILES * 4 * 52)

    # Calculate the total cost of the miles driven
    miles_cost = yearly_miles * PRICE_PER_MILE

    # Calculate the total cost for the weekly fees
    weekly_fees = WEEKLY_FEE * 52

    # Calculate the total cost for the year
    total_cost = miles_cost + weekly_fees

    # Display the total cost for the year
    result = total_cost
    return result

print(solution())