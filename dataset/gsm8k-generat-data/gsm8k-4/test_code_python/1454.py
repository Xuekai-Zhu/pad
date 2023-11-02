def solution():
    """Tom decides to lease a car. He drives 50 miles on Monday, Wednesday, and Friday, and Sunday for the rest of the days he drives 100 miles. He has to pay $.1 per mile he drives. He also has to pay a weekly fee of $100. How much does he have to pay in a year."""
    # Define the number of days in a week and a year
    DAYS_IN_WEEK = 7
    DAYS_IN_YEAR = 365

    # Define the daily mileage
    monday_mileage = 50
    wednesday_mileage = 50
    friday_mileage = 50
    rest_mileage = 100

    # Calculate the total annual mileage
    annual_mileage = (monday_mileage + wednesday_mileage + friday_mileage) * 3 + rest_mileage * (DAYS_IN_YEAR - 3*DAYS_IN_WEEK)

    # Calculate the annual cost of the mileage
    mileage_cost = annual_mileage * 0.1

    # Calculate the annual cost of the weekly fee
    weekly_fee_cost = 100 * (DAYS_IN_YEAR // DAYS_IN_WEEK)

    # Calculate the total annual cost
    total_cost = mileage_cost + weekly_fee_cost

    result = total_cost
    return result

print(solution())