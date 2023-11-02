def solution():
    """There are 20 cars lined up at a race. Each of the cars have 2 passengers and a driver, then when the cars go past the race’s halfway point, each car gains another passenger. The cars then continue racing, and the race finishes once every single car has passed the finish line. People who get into the cars have to stay inside of them until the race is finished. How many people are in the cars by the end of the race?"""
    cars = 20
    passengers_per_car = 2
    drivers_per_car = 1
    total_people = cars * (passengers_per_car + drivers_per_car)
    
    # After the halfway point, each car gains another passenger
    extra_passengers_per_car = 1
    cars_after_halfway_point = cars // 2
    total_extra_passengers = cars_after_halfway_point * extra_passengers_per_car
    
    result = total_people + total_extra_passengers
    return result

print(solution())