def solution():
    """A plane travels 1200 miles in 3 hours. At the same rate, how many additional hours would it take to travel an additional 2000 miles?"""
    distance = 1200
    time = 3
    rate = distance / time
    additional_distance = 2000
    additional_time = additional_distance / rate
    result = additional_time - time
    
    return result

print(solution())