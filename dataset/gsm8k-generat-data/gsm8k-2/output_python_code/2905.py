def solution():
    """There are 20 bicycles, 10 cars and 5 motorcycles in the garage at Connor's house. How many wheels are there in the garage?"""
    bicycle_wheels = 2 * 20
    car_wheels = 4 * 10
    motorcycle_wheels = 2 * 5
    total_wheels = bicycle_wheels + car_wheels + motorcycle_wheels
    result = total_wheels
    return result

print(solution())