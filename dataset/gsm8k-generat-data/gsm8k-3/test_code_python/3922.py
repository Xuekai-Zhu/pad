def solution():
    """A car manufacturing company that produces 100 cars per month wants to increase its production to reach 1800 cars per year. How many cars should the company add to the monthly production rate to reach that target?"""
    # Define the current production rate and target production rate
    CURRENT_PRODUCTION_RATE = 100
    TARGET_PRODUCTION_RATE = 150

    # Calculate the additional cars needed per month
    additional_cars_per_month = (TARGET_PRODUCTION_RATE - CURRENT_PRODUCTION_RATE) / 12

    # Display the additional cars needed per month
    result = additional_cars_per_month
    return result

print(solution())