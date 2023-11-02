def solution():
    """Wynter went to her local town bike shop to buy her sister a bicycle as her birthday gift. While at the shop, Wynter counted 50 bicycles and 20 tricycles. How many wheels in total did the vehicles she saw have?"""
    # Define the number of bicycles and tricycles
    bicycles = 50
    tricycles = 20

    # Calculate the total number of wheels on the bicycles
    bicycle_wheels = bicycles * 2

    # Calculate the total number of wheels on the tricycles
    tricycle_wheels = tricycles * 3

    # Calculate the total number of wheels
    total_wheels = bicycle_wheels + tricycle_wheels

    # return the result
    result = total_wheels
    return result

print(solution())