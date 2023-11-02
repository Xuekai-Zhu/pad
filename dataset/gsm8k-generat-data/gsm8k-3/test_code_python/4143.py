def solution():
    """There are 20 cars lined up at a race. Each of the cars have 2 passengers and a driver, then when the cars go past the race’s halfway point, each car gains another passenger. The cars then continue racing, and the race finishes once every single car has passed the finish line. People who get into the cars have to stay inside of them until the race is finished. How many people are in the cars by the end of the race?"""
    # Define the number of cars and initial number of passengers
    num_cars = 20
    initial_passengers = 3

    # Calculate the number of passengers after the halfway point
    after_halfway_passengers = initial_passengers + 1

    # Calculate the total number of passengers before and after the halfway point
    before_halfway_passengers = initial_passengers * num_cars
    total_passengers = before_halfway_passengers + (num_cars * after_halfway_passengers)

    # Display the total number of passengers in the cars
    result = total_passengers
    return result

print(solution())