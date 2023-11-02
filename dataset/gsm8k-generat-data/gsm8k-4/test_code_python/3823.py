def solution():
    """The garbage truck passes through Daniel's neighborhood on Tuesdays, Thursdays, and Saturdays. In each garbage collection, an average of 200 kg is taken. Due to obstruction in the roads leading to Daniel's neighborhood, the garbage truck stops passing through for two weeks. During the first week, people in Daniel's neighborhood pile the extra garbage around the dumpster, during the second week they apply a policy of cutting their amount of garbage in half. How many kilograms of garbage have accumulated in Daniel's neighborhood during the 2 weeks?"""
    # Define the average amount of garbage collected in each collection
    GARBAGE_PER_COLLECTION = 200

    # Define the number of collection days in a week
    COLLECTION_DAYS_PER_WEEK = 3

    # Define the number of weeks without garbage collection
    WEEKS_WITHOUT_COLLECTION = 2

    # Calculate the total amount of garbage accumulated during the first week
    week_one_garbage = GARBAGE_PER_COLLECTION * COLLECTION_DAYS_PER_WEEK

    # Calculate the total amount of garbage accumulated during the second week
    week_two_garbage = (GARBAGE_PER_COLLECTION / 2) * COLLECTION_DAYS_PER_WEEK

    # Calculate the total amount of garbage accumulated during the two weeks
    total_garbage = (week_one_garbage + week_two_garbage) * WEEKS_WITHOUT_COLLECTION
    
    result = total_garbage
    return result

print(solution())