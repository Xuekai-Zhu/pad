def solution():
    """It takes 1 hour for refrigerated dough to come to room temperature. It takes 15 minutes to shape the dough and 2 hours to proof. The bread takes 30 minutes to bake and 15 minutes to cool. If the bakery opens at 6:00 am, what is the latest time the head baker can make it to the store to start working?"""
    
    # Define the total time needed to make the bread
    total_time = 1*60 + 15 + 2*60 + 30 + 15

    # Calculate the latest time the head baker can make it to the store
    latest_time = "4:" + str(60 - total_time//60).zfill(2) + " am"

    result = latest_time
    return result

print(solution())