def solution():
    """Audrey was asleep for 10 hours last night and dreamed for 2/5 of the time. How much of the night was she not dreaming?"""
    # Define the total number of hours Audrey was asleep
    total_hours = 10

    # Calculate the number of hours Audrey was dreaming
    dreaming_hours = total_hours * (2/5)

    # Calculate the number of hours Audrey was not dreaming
    not_dreaming_hours = total_hours - dreaming_hours

    # Display the number of hours Audrey was not dreaming
    result = not_dreaming_hours
    return result

print(solution())