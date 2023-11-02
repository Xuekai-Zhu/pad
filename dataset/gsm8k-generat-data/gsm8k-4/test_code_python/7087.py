def solution():
    """To earn an airplane pilot certificate, Sangita is required to fly 1,500 hours. She has already completed 50 hours of day flying, 9 hours of night flying, and 121 hours flying cross-country. To meet her goal in exactly 6 months, how many hours per month must Sangita fly?"""
    # Define the total required flying hours and the completed hours
    required_hours = 1500
    completed_hours = 50 + 9 + 121

    # Calculate the remaining hours to complete
    remaining_hours = required_hours - completed_hours

    # Calculate the required flying hours per month to complete in 6 months
    flying_hours_per_month = remaining_hours / 6

    result = flying_hours_per_month
    return result

print(solution())