def solution():
    """There are 20 cars lined up at a race. Each of the cars have 2 passengers and a driver, then when the cars go past the race’s halfway point, each car gains another passenger. The cars then continue racing, and the race finishes once every single car has passed the finish line. People who get into the cars have to stay inside of them until the race is finished. How many people are in the cars by the end of the race?"""
    cars = 20
    initial_passengers_per_car = 2
    additional_passengers_per_car = 1
    halfway_point = cars / 2
    
    # Calculate number of passengers for cars before halfway point
    initial_passengers = cars * initial_passengers_per_car
    
    # Calculate number of passengers for cars after halfway point
    additional_cars = cars - halfway_point
    additional_passengers = additional_cars * additional_passengers_per_car
    
    total_passengers = initial_passengers + additional_passengers
    result = total_passengers
    return result

print(solution())