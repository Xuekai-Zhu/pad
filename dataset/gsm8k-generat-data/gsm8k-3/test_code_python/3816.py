def solution():
    """Goldie makes $5 an hour for pet-sitting. Last week, she worked for 20 hours while this week, she worked for 30 hours. How much did Goldie earn in two weeks for pet-sitting?"""
    # Define Goldie's hourly rate
    HOURLY_RATE = 5

    # Get the number of hours Goldie worked in the last two weeks
    total_hours = 20 + 30

    # Calculate Goldie's earnings
    earnings = total_hours * HOURLY_RATE

    # Display Goldie's earnings
    result = earnings
    return result

print(solution())