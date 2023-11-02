def solution():
    """A performing magician has a disappearing act where he makes a random member of his audience disappear and reappear. Unfortunately, one-tenth of the time, the audience member never reappears. However, one-fifth of the time, two people reappear instead of only one. If the magician has put on 100 performances of the act this year, how many people have reappeared?"""
    # Define the total number of performances and initialize the number of people who have reappeared
    total_performances = 100
    reappeared_people = 0

    # Calculate the number of people who reappear and add it to the total
    for i in range(total_performances):
        # Generate a random number between 1 and 10
        rand_num = random.randint(1,10)

        # If the random number is 1, the person never reappears
        if rand_num == 1:
            pass
        # If the random number is 2 or 3, two people reappear
        elif rand_num in [2,3]:
            reappeared_people += 2
        # Otherwise, one person reappears
        else:
            reappeared_people += 1

    # Return the total number of people who have reappeared
    result = reappeared_people
    return result

print(solution())