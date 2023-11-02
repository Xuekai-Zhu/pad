def solution():
    """It takes 1 hour for refrigerated dough to come to room temperature. It takes 15 minutes to shape the dough and 2 hours to proof. The bread takes 30 minutes to bake and 15 minutes to cool. If the bakery opens at 6:00 am, what is the latest time the head baker can make it to the store to start working?"""
    total_time = 1 + (15/60) + 2 + (30/60) + (15/60) # in hours
    open_time = 6
    latest_arrival_time = open_time - total_time
    result = latest_arrival_time
    return result

print(solution())