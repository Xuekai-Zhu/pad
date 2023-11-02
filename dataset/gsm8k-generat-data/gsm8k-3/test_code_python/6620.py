def solution():
    """Robby, Jaylen and Miranda are employed at a Cheesecake factory, earning $10 per hour. They work 10 hours a day, five days a week. Robby saves 2/5 of his salary, Jaylene saves 3/5 of his salary, while Miranda saves half of her salary. What are the combined savings of the three employees after four weeks?"""
    # Define the hourly rate and the number of working hours
    HOURLY_RATE = 10
    WORKING_HOURS = 10 * 5

    # Calculate the total earnings for each employee per week
    weekly_earnings = HOURLY_RATE * WORKING_HOURS

    # Calculate the savings for each employee per week
    robby_savings = 2/5 * weekly_earnings
    jaylene_savings = 3/5 * weekly_earnings
    miranda_savings = 1/2 * weekly_earnings

    # Calculate the total savings for all three employees after four weeks
    total_savings = 4 * (robby_savings + jaylene_savings + miranda_savings)

    # Display the total savings
    result = total_savings
    return result

print(solution())