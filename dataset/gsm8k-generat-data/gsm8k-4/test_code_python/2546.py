def solution():
    """Jack makes his own cold brew coffee. He makes it in batches of 1.5 gallons. He drinks 96 ounces of coffee every 2 days. It takes 20 hours to make coffee. How long does he spend making coffee over 24 days?"""
    # Define the batch size and conversion factors
    BATCH_SIZE = 1.5 * 128  # 1 gallon = 128 ounces
    OUNCES_PER_DAY = 96
    HOURS_PER_BATCH = 20

    # Calculate the number of batches in 24 days
    batches = 24 * 60 // 2  # 24 days * 60 minutes / day / 2 days / batch = 720 / 2 = 360 batches

    # Calculate the total amount of coffee made
    total_coffee = batches * BATCH_SIZE

    # Calculate the number of days worth of coffee this is
    days_of_coffee = total_coffee // OUNCES_PER_DAY

    # Calculate the total number of hours spent making coffee
    total_hours = batches * HOURS_PER_BATCH

    result = total_hours
    return result

print(solution())