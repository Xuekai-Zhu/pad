def solution():
    """Jack makes his own cold brew coffee.  He makes it in batches of 1.5 gallons.  He drinks 96 ounces of coffee every 2 days.  It takes 20 hours to make coffee.  How long does he spend making coffee over 24 days?"""
    # Define the variables
    BATCH_SIZE = 1.5 * 128  # 1.5 gallons in ounces
    DRINKS_PER_DAY = 96 / 2  # 96 ounces every 2 days
    HOURS_PER_BATCH = 20
    DAYS = 24

    # Calculate the number of batches needed
    batches_needed = DAYS * DRINKS_PER_DAY / BATCH_SIZE

    # Calculate the total time spent making coffee
    time_spent = batches_needed * HOURS_PER_BATCH

    # Display the time spent making coffee
    result = time_spent
    return result

print(solution())