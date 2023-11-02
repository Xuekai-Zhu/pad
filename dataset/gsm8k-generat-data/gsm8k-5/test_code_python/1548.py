def solution():
    starting_bugs = 400  # The garden has 400 bugs to start
    sprayed_bugs = starting_bugs * 0.8  # After spraying, the bug population is reduced to 80% of what it was previously
    introduced_spiders = 12  # Bill introduces 12 spiders, each of which eats 7 bugs

    # Calculate the total number of bugs eaten by the spiders
    total_bugs_eaten = introduced_spiders * 7

    # Calculate the remaining number of bugs in the garden
    remaining_bugs = sprayed_bugs - total_bugs_eaten
    result = remaining_bugs
    return result

print(solution())