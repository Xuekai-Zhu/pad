def solution():
    """Kevin has a shoebox filled with toads.  Every day, Kevin feeds each toad 3 worms.  It takes Kevin 15 minutes to find each worm.  If it takes Kevin 6 hours to find enough worms to feed all of his toads, how many toads does Kevin have in his shoebox?"""
    # Convert 6 hours to minutes
    time_in_minutes = 6 * 60

    # Calculate how many worms Kevin can find in that time
    worms_found = time_in_minutes // 15

    # Calculate how many toads Kevin can feed with those worms
    toads_fed = worms_found // 3

    # Display the number of toads
    result = toads_fed
    return result

print(solution())