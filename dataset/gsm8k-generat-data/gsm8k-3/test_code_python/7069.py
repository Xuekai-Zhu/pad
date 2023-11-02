def solution():
    """It is the rainy season in central Texas.  It rained for 7 hours on Monday at a rate of 1 inch per hour.  On Tuesday, it rained for 4 hours at a rate of 2 inches per hour, and on Wednesday, it rained for 2 hours at a rate of twice that of the previous day.  What is the total combined rainfall, in inches, for these three days?"""
    # Calculate the total rainfall on Monday
    monday_rainfall = 7 * 1

    # Calculate the total rainfall on Tuesday
    tuesday_rainfall = 4 * 2

    # Calculate the total rainfall on Wednesday
    wednesday_rainfall = 2 * 2 * 2

    # Calculate the total combined rainfall
    total_rainfall = monday_rainfall + tuesday_rainfall + wednesday_rainfall

    # Display the total combined rainfall
    result = total_rainfall
    return result

print(solution())