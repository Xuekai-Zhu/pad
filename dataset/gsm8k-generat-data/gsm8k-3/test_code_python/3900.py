def solution():
    """If the wages of 15 workers for 6 days is $9450. What would be the wages for 19 workers for 5 days?"""
    # Define the variables
    workers1 = 15
    days1 = 6
    wages1 = 9450
    workers2 = 19
    days2 = 5

    # Calculate the wages for 1 worker in one day
    wages_per_worker_per_day = wages1 / (workers1 * days1)

    # Calculate the total wages for 19 workers in 5 days
    wages2 = wages_per_worker_per_day * (workers2 * days2)

    # Display the total wages for 19 workers in 5 days
    result = wages2
    return result

print(solution())