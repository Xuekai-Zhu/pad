def solution():
    """Lake Crystal has twenty percent fewer frogs than Lassie Lake. If Lassie Lake has forty-five frogs, how many frogs are there in total in the two lakes?"""
    # Define the number of frogs in Lassie Lake
    lassie_frogs = 45

    # Calculate the number of frogs in Lake Crystal
    crystal_frogs = lassie_frogs * 0.8

    # Calculate the total number of frogs in both lakes
    total_frogs = lassie_frogs + crystal_frogs

    # return the result
    result = total_frogs
    return result

print(solution())