def solution():
    """Of the 20 available cars for rent, 12 are automatic cars, 4 are manual cars, and the rest are semi-automatic. What percentage of the cars are semi-automatic?"""
    total_cars = 20
    auto_cars = 12
    manual_cars = 4
    semi_auto_cars = total_cars - auto_cars - manual_cars
    semi_auto_percent = (semi_auto_cars / total_cars) * 100
    result = semi_auto_percent
    
    return result

print(solution())