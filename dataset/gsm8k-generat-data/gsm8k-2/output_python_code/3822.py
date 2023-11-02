def solution():
    """The garbage truck passes through Daniel's neighborhood on Tuesdays, Thursdays, and Saturdays. In each garbage collection, an average of 200 kg is taken. Due to obstruction in the roads leading to Daniel's neighborhood, the garbage truck stops passing through for two weeks. During the first week, people in Daniel's neighborhood pile the extra garbage around the dumpster, during the second week they apply a policy of cutting their amount of garbage in half. How many kilograms of garbage have accumulated in Daniel's neighborhood during the 2 weeks?"""
    garbage_per_collection = 200
    collections_per_week = 3
    weeks_without_pickup = 2
    garbage_accumulated_first_week = garbage_per_collection * collections_per_week * weeks_without_pickup
    garbage_accumulated_second_week = garbage_accumulated_first_week / 2
    total_garbage_accumulated = garbage_accumulated_first_week + garbage_accumulated_second_week
    result = total_garbage_accumulated
    return result

print(solution())