def solution():
    """John repairs 5 cars. 3 of the cars take 40 minutes each to repair. The remaining ones take 50% longer each to repair. He makes $20 per hour repairing cars. How much money does he make?"""
    hourly_rate = 20
    car_rate = 5
    normal_time = 40
    extra_time = normal_time * 1.5
    normal_cars = 3
    extra_cars = car_rate - normal_cars
    normal_earnings = (normal_cars * normal_time / 60) * hourly_rate
    extra_earnings = (extra_cars * extra_time / 60) * hourly_rate
    total_earnings = normal_earnings + extra_earnings
    result = total_earnings
    return result

print(solution())