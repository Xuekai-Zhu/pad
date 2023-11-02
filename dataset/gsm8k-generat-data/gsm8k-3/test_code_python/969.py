def solution():
    """Lake Crystal has twenty percent fewer frogs than Lassie Lake. If Lassie Lake has forty-five frogs, how many frogs are there in total in the two lakes?"""
    # Define the number of frogs in Lassie Lake and Lake Crystal
    lassie_frogs = 45
    crystal_frogs = 0.8 * lassie_frogs

    # Calculate the total number of frogs in both lakes
    total_frogs = lassie_frogs + crystal_frogs

    # Display the total number of frogs
    result = total_frogs
    return result

print(solution())