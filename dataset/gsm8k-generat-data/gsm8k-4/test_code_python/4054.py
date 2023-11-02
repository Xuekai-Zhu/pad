def solution():
    """John has to hire a lawyer. He pays $1000 upfront. He then gets charged $100 per hour. The lawyer has to work 50 hours in court time. It takes 2 times that long in prep time. His brother pays half the fee. How much did John pay?"""
    # Define the variables
    upfront_fee = 1000
    hourly_rate = 100
    court_time = 50
    prep_time = 2 * court_time
    total_hours = court_time + prep_time

    # Calculate the total fee charged by the lawyer
    total_fee = (total_hours * hourly_rate) + upfront_fee

    # Calculate John's share of the fee after his brother paid half
    john_fee = (total_fee / 2) - upfront_fee

    # Return the result
    result = john_fee
    return result

print(solution())