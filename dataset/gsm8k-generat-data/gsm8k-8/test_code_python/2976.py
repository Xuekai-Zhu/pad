def solution():
    # Calculate the number of fences Abigail can build in 1 hour
    fences_per_hour = 2

    # Calculate the total number of hours Abigail will work
    total_hours_worked = 8

    # Calculate the total number of fences Abigail will build in 8 hours
    total_fences_built = fences_per_hour * total_hours_worked

    # Add the initial 10 fences Abigail built to find the total number of fences
    total_fences = total_fences_built + 10
    result = total_fences
    return result

print(solution())