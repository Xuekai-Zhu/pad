def solution():
    """John has to hire a lawyer.  He pays $1000 upfront.  He then gets charged $100 per hour.  The lawyer has to work 50 hours in court time.  It takes 2 times that long in prep time.  His brother pays half the fee.  How much did John pay?"""
    # Define the cost of upfront payment and hourly rate of the lawyer
    UPFRONT_PAY = 1000
    HOURLY_RATE = 100

    # Calculate the total cost of the lawyer's court time
    court_time = 50
    court_time_cost = court_time * HOURLY_RATE

    # Calculate the total prep time for the lawyer
    prep_time = 2 * court_time

    # Calculate the total cost of the lawyer's prep time
    prep_time_cost = prep_time * HOURLY_RATE

    # Calculate the total cost of the lawyer's services
    total_cost = UPFRONT_PAY + court_time_cost + prep_time_cost

    # Calculate the amount John's brother pays
    brother_cost = total_cost / 2

    # Calculate the amount John pays
    john_cost = total_cost - brother_cost

    # Display the amount John pays
    result = john_cost
    return result

print(solution())