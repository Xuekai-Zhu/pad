def solution():
    # Define the end of the Middle Ages and the invention of dynamite
    middle_ages_end = 1453
    dynamite_invented = 1870
    # Check if dynamite was invented after the Middle Ages ended
    if dynamite_invented > middle_ages_end:
        result = "no"
    else:
        result = "yes"
    return result

print(solution())