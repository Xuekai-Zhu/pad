def solution():
    # Year 1: 4 statues created
    statues = 4

    # Year 2: quadrupled number of statues
    statues *= 4

    # Year 3: added 12 statues, but 3 were broken and thrown away
    statues += 12
    statues -= 3

    # Year 4: added twice as many new statues as had been broken the year before
    statues += 2 * 3

    result = statues
    return result

print(solution())