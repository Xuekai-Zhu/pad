def solution():
    """The garbage truck passes through Daniel's neighborhood on Tuesdays, Thursdays, and Saturdays. In each garbage collection, an average of 200 kg is taken. Due to obstruction in the roads leading to Daniel's neighborhood, the garbage truck stops passing through for two weeks. During the first week, people in Daniel's neighborhood pile the extra garbage around the dumpster, during the second week they apply a policy of cutting their amount of garbage in half. How many kilograms of garbage have accumulated in Daniel's neighborhood during the 2 weeks?"""
    # Define the average amount of garbage collected in each collection
    GARBAGE_COLLECTED_PER_COLLECTION = 200

    # Define the number of garbage collections missed during the two weeks
    NUM_COLLECTIONS_MISSED = 3 * 2

    # Calculate the amount of garbage that would have been collected during the two missed weeks
    missed_garbage = GARBAGE_COLLECTED_PER_COLLECTION * NUM_COLLECTIONS_MISSED

    # Calculate the amount of garbage piled up during the first week
    week1_garbage = missed_garbage

    # Calculate the amount of garbage left during the second week
    week2_garbage = week1_garbage / 2

    # Calculate the total amount of garbage accumulated during the 2 weeks
    total_garbage = week1_garbage + week2_garbage

    # Display the total amount of garbage accumulated
    result = total_garbage
    return result

print(solution())