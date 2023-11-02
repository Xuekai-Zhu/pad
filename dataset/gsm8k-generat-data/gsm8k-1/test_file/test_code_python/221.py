def solution():
    """Andrew plans a road trip from New Jersey to Rochester. It takes 6 days to travel by bus and half as many days to travel by car from New Jersey to Rochester. How many days will he travel if he plans to go to Rochester by bus and return from Rochester by car?"""
    bus_days = 6
    car_days = bus_days / 2
    total_days = bus_days + car_days
    result = total_days
    return result

print(solution())