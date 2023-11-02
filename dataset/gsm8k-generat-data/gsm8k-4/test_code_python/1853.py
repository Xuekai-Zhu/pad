def solution():
    """How many shirts should Shenny pack for her next vacation if she's planning to use the same shirt when departing on Monday and returning on Sunday and two different shirts each other day?"""
    # Define the number of days for the vacation
    vacation_days = 7

    # Calculate the number of shirts needed for Monday and Sunday
    monday_sunday_shirts = 1

    # Calculate the number of shirts needed for the rest of the days
    other_days_shirts = (vacation_days - 2) * 2

    # Calculate the total number of shirts needed
    total_shirts = monday_sunday_shirts + other_days_shirts

    # Return the result
    result = total_shirts
    return result

print(solution())