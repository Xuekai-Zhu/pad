def solution():
    """Wynter went to her local town bike shop to buy her sister a bicycle as her birthday gift. While at the shop, Wynter counted 50 bicycles and 20 tricycles. How many wheels in total did the vehicles she saw have?"""
    bike_wheels = 2
    trike_wheels = 3
    total_bikes = 50
    total_trikes = 20
    total_wheels = total_bikes * bike_wheels + total_trikes * trike_wheels
    result = total_wheels
    return result

print(solution())