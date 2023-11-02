def solution():
    """If 3 crows eat 30 worms in one hour, how many worms will 5 crows eat in 2 hours?"""
    # Define the number of crows and worms per hour
    crows = 3
    worms_per_hour = 30

    # Calculate the total number of worms eaten by 3 crows in 2 hours
    worms_3_crows_2_hours = worms_per_hour * 3 * 2

    # Calculate the number of worms eaten by 1 crow in 1 hour
    worms_per_crow_per_hour = worms_per_hour / crows

    # Calculate the total number of worms eaten by 5 crows in 2 hours
    worms_5_crows_2_hours = worms_per_crow_per_hour * 5 * 2

    # Return the result
    result = worms_5_crows_2_hours
    return result

print(solution())