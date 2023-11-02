def solution():
    """Sam earns $10 an hour on Math tutoring. For the first month, he earned $200; and for the second month, he earned $150 more than the first month. How many hours did he spend on tutoring for two months?"""
    # Define the hourly rate
    HOURLY_RATE = 10

    # Define the earnings for the first month and calculate the hours worked
    earnings_1 = 200
    hours_1 = earnings_1 / HOURLY_RATE

    # Define the earnings for the second month and calculate the hours worked
    earnings_2 = earnings_1 + 150
    hours_2 = earnings_2 / HOURLY_RATE

    # Calculate the total hours worked
    total_hours = hours_1 + hours_2

    # Display the total hours worked
    result = total_hours
    return result

print(solution())