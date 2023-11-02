def solution():
    """Wynter went to her local town bike shop to buy her sister a bicycle as her birthday gift. While at the shop, Wynter counted 50 bicycles and 20 tricycles. How many wheels in total did the vehicles she saw have?"""
    # Define the number of wheels on a bicycle and a tricycle
    BICYCLE_WHEELS = 2
    TRICYCLE_WHEELS = 3

    # Determine the total number of wheels on the bicycles
    bicycle_wheels = 50 * BICYCLE_WHEELS

    # Determine the total number of wheels on the tricycles
    tricycle_wheels = 20 * TRICYCLE_WHEELS

    # Determine the total number of wheels on all the vehicles
    total_wheels = bicycle_wheels + tricycle_wheels

    # Display the total number of wheels
    result = total_wheels
    return result

print(solution())