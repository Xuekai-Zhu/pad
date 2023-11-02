def solution():
    """Jeff had 300 pencils and donated 30% of them. Vicki had twice as many pencils as Jeff and donated 3/4 of his pencils. How many pencils are there remaining altogether?"""
    # Define Jeff's initial number of pencils and the percentage he donated
    JEFF_PENCILS = 300
    JEFF_DONATED_PERCENTAGE = 0.3

    # Calculate how many pencils Jeff has left after donating
    jeff_remaining = JEFF_PENCILS * (1 - JEFF_DONATED_PERCENTAGE)

    # Define Vicki's initial number of pencils and how many he donated
    VICKI_PENCILS = 2 * JEFF_PENCILS
    VICKI_DONATED = 0.75 * VICKI_PENCILS

    # Calculate how many pencils Vicki has left after donating
    vicki_remaining = VICKI_PENCILS - VICKI_DONATED

    # Calculate the total number of pencils remaining
    total_remaining = jeff_remaining + vicki_remaining

    # Display the total number of pencils remaining
    result = total_remaining
    return result

print(solution())