def solution():
    """From Monday to Friday, Elle practices piano for 30 minutes. On Saturday, she practices piano three times as much as on a weekday. There is no practice on Sunday.  How many hours does Elle spend practicing piano each week?"""
    # Define the length of a weekday practice session in hours
    WEEKDAY_PRACTICE = 0.5/60  # 0.5 hours = 30 minutes

    # Calculate the length of a Saturday practice session in hours
    SATURDAY_PRACTICE = 3 * WEEKDAY_PRACTICE

    # Calculate the total practice time for the week
    total_practice = 5 * WEEKDAY_PRACTICE + SATURDAY_PRACTICE

    # Display the total practice time for the week in hours
    result = total_practice
    return result

print(solution())