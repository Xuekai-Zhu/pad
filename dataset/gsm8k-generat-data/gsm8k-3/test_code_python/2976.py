def solution():
    """Abigail built 10 fences. Each fence took her 30 minutes to build. If she builds fences for the next 8 hours, how many fences would she have built in total?"""
    # Define the number of fences built per hour
    FENCES_PER_HOUR = 2

    # Calculate the total number of hours Abigail works
    total_hours = 8

    # Calculate the total number of fences Abigail can build in the given time
    total_fences = FENCES_PER_HOUR * total_hours + 10

    # Display the total number of fences Abigail built
    result = total_fences
    return result

print(solution())