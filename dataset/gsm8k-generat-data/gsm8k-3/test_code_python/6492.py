def solution():
    """If 3 crows eat 30 worms in one hour, how many worms will 5 crows eat in 2 hours?"""
    # Define the number of crows and worms eaten in one hour
    crows_per_hour = 3
    worms_per_hour = 30

    # Calculate the total number of worms eaten in two hours by 5 crows
    worms_2_hours = 5 * worms_per_hour * 2 / crows_per_hour

    # Display the total number of worms eaten
    result = worms_2_hours
    return result

print(solution())