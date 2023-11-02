def solution():
    """Cary is trying to strip the ivy off a tree in her yard. She strips 6 feet of ivy every day, but the ivy grows another 2 feet every night. If the tree is covered by 40 feet of ivy, how many days will it take Cary to strip all the ivy off?"""
    # Initialize variables
    ivy_left = 40
    days = 0

    # While loop to strip the ivy
    while ivy_left > 0:
        ivy_left -= 6 # Cary strips 6 feet of ivy
        if ivy_left <= 0:
            break # exit loop if all ivy is stripped
        ivy_left += 2 # Ivy grows 2 feet every night
        days += 1 # Add 1 day to the count

    # Display the number of days it takes to strip all the ivy
    result = days
    return result

print(solution())