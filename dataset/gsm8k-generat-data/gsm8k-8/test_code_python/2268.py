def solution():
    # Calculate the time Kevin spends finding worms
    worm_finding_time = 6 * 60  # in minutes
    worms_needed = None  # we need to find this value
    worms_finding_time = None  # we need to find this value

    # Use a loop to iterate through different values of worms_needed until we find the correct value
    for i in range(1, 21):
        worms_needed = i  # test each value from 1 to 20
        worms_finding_time = worms_needed * 3 * 15  # calculate the time it takes to find that many worms
        if worms_finding_time == worm_finding_time:  # if the total worm-finding time equals the time Kevin has available
            break  # we've found the correct value of worms_needed

    # Calculate the number of toads
    toads = worms_needed * 10  # each toad eats 3 worms per day, and Kevin has 10 days' worth of worms
    result = toads
    return result

print(solution())