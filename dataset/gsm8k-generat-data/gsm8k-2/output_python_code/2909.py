def solution():
    """At a station, a train comes every 5 minutes leaving 200 passengers and taking 320 others. How many different passengers step on and off a train at the station within an hour?"""
    passengers_per_train = 120
    trains_per_hour = 60 // 5  # 12 trains per hour
    total_leaving = passengers_per_train * trains_per_hour
    total_taking = (passengers_per_train + 200) * trains_per_hour
    total_passengers = total_leaving + total_taking
    result = total_passengers
    return result

print(solution())