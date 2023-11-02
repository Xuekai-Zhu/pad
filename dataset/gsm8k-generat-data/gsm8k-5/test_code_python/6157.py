def solution():
    performances = 100  # The magician has put on 100 performances
    people_disappeared = performances  # Each performance makes one person disappear
    people_reappeared = 0  # Initialize the count of people who have reappeared

    for performance in range(performances):
        # One-tenth of the time, the person never reappears
        if random.random() < 0.1:
            people_disappeared -= 1
        # One-fifth of the time, two people reappear
        elif random.random() < 0.2:
            people_reappeared += 2
        # Otherwise, only one person reappears
        else:
            people_reappeared += 1

    result = people_reappeared
    return result

print(solution())