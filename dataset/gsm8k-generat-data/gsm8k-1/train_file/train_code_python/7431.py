def solution():
    """It takes 10 minutes to wash a car, 15 minutes to change oil, and 30 minutes to change a set of tires. If mike washes 9 cars, changes the oil on 6 cars, and changes two sets of tires how many hours did he work?"""
    wash_time = 10
    oil_change_time = 15
    tire_change_time = 30
    cars_washed = 9
    oil_changes = 6
    tire_changes = 2
    total_time = (wash_time * cars_washed) + (oil_change_time * oil_changes) + (tire_change_time * tire_changes)
    total_hours = total_time / 60
    result = total_hours
    return result

print(solution())