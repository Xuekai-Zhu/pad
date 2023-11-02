def solution():
    # Define the starting bug population and number of spiders
    starting_bugs = 400
    spiders = 12

    # Calculate the number of bugs eaten by the spiders
    bugs_eaten_by_spiders = spiders * 7

    # Reduce the total bug population after spraying
    after_spray = starting_bugs * 0.8

    # Calculate the final bug population after introducing spiders
    final_bugs = after_spray - bugs_eaten_by_spiders
    result = final_bugs
    return result

print(solution())