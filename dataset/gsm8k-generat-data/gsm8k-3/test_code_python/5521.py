def solution():
    """It takes 1 hour for refrigerated dough to come to room temperature.  It takes 15 minutes to shape the dough and 2 hours to proof.  The bread takes 30 minutes to bake and 15 minutes to cool.  If the bakery opens at 6:00 am, what is the latest time the head baker can make it to the store to start working?"""
    # Define the time it takes to prepare the dough
    DOUGH_PREP_TIME = 1

    # Define the time it takes to shape the dough
    DOUGH_SHAPING_TIME = 0.25

    # Define the time it takes to proof the dough
    DOUGH_PROOFING_TIME = 2

    # Define the time it takes to bake the bread
    BAKING_TIME = 0.5

    # Define the time it takes to cool the bread
    COOLING_TIME = 0.25

    # Define the bakery's opening time
    OPENING_TIME = 6

    # Calculate the total time required to make the bread
    total_time = DOUGH_PREP_TIME + DOUGH_SHAPING_TIME + DOUGH_PROOFING_TIME + BAKING_TIME + COOLING_TIME

    # Calculate the latest time the head baker can arrive to start working
    latest_arrival_time = OPENING_TIME - total_time

    # Display the latest arrival time
    result = latest_arrival_time
    return result

print(solution())