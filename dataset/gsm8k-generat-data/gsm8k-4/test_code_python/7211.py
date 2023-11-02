def solution():
    """Cary is trying to strip the ivy off a tree in her yard. She strips 6 feet of ivy every day, but the ivy grows another 2 feet every night. If the tree is covered by 40 feet of ivy, how many days will it take Cary to strip all the ivy off?"""
    # Define the initial length of ivy and the daily stripping and growing
    ivy_length = 40
    daily_strip = 6
    nightly_grow = 2

    # Initialize the day counter and the remaining ivy length
    days = 0
    remaining_ivy = ivy_length

    # Loop until all ivy is stripped
    while remaining_ivy > 0:
        # Increment the day counter
        days += 1

        # Strip the daily amount of ivy
        remaining_ivy -= daily_strip

        # If all ivy is stripped, exit the loop
        if remaining_ivy <= 0:
            break

        # Let the ivy grow overnight
        remaining_ivy += nightly_grow

    # Display the number of days it took to strip all the ivy
    result = days
    return result

print(solution())