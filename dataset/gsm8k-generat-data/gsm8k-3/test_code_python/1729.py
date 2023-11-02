def solution():
    """Calvin is a bug collector.  In his collection, he has 12 giant roaches, 3 scorpions, half as many crickets as roaches, and twice as many caterpillars as scorpions.  How many insects does Calvin have in his collection?"""
    # Define the number of each type of bug in Calvin's collection
    roaches = 12
    scorpions = 3
    crickets = roaches / 2
    caterpillars = scorpions * 2

    # Calculate the total number of bugs in his collection
    total_bugs = roaches + scorpions + crickets + caterpillars

    # Display the total number of bugs
    result = total_bugs
    return result

print(solution())