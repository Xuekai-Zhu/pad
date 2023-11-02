def solution():
    """It takes 10 minutes to wash a car, 15 minutes to change oil, and 30 minutes to change a set of tires. If Mike washes 9 cars, changes the oil on 6 cars, and changes two sets of tires how many hours did he work?"""
    wash_time = 10
    oil_time = 15
    tire_time = 30
    total_time = (wash_time * 9) + (oil_time * 6) + (tire_time * 2)
    total_hours = total_time / 60
    result = total_hours
    return result

print(solution())