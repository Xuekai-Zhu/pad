def solution():
    """During one day, there are 4 boat trips through the lake. The boat can take up to 12 people during one trip. How many people can the boat transport in 2 days?"""
    trips_per_day = 4
    capacity_per_trip = 12
    days = 2
    total_people = trips_per_day * capacity_per_trip * days
    result = total_people
    return result

print(solution())