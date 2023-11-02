def solution():
    """The chocolate factory produces 50 candies per hour. It has to fulfill an order and produce 4000 candies. How many days will it take to complete the order if the factory works for 10 hours every day?"""
    # Define the production rate per hour
    PRODUCTION_RATE = 50

    # Define the target number of candies to produce
    TARGET = 4000

    # Define the number of hours worked per day
    HOURS_PER_DAY = 10

    # Calculate the number of days required to fulfill the order
    candies_per_day = PRODUCTION_RATE * HOURS_PER_DAY
    days_needed = TARGET // candies_per_day
    if TARGET % candies_per_day != 0:
        days_needed += 1

    # Display the number of days needed
    result = days_needed
    return result

print(solution())