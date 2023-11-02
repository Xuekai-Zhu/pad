def solution():
    """To earn an airplane pilot certificate, Sangita is required to fly 1,500 hours. She has already completed 50 hours of day flying, 9 hours of night flying, and 121 hours flying cross-country. To meet her goal in exactly 6 months, how many hours per month must Sangita fly?"""
    # Define the total number of required hours
    TOTAL_HOURS = 1500

    # Define the number of hours completed so far
    completed_hours = 50 + 9 + 121

    # Define the number of remaining hours
    remaining_hours = TOTAL_HOURS - completed_hours

    # Calculate the required number of hours per month
    required_hours = remaining_hours / 6

    # Display the required number of hours per month
    result = required_hours
    return result

print(solution())