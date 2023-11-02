def solution():
    """There are 20 cars lined up at a race. Each of the cars have 2 passengers and a driver, then when the cars go past the race’s halfway point, each car gains another passenger. The cars then continue racing, and the race finishes once every single car has passed the finish line. People who get into the cars have to stay inside of them until the race is finished. How many people are in the cars by the end of the race?"""
    # Define the number of cars
    cars = 20

    # Define the initial number of people in the cars
    initial_people = cars * 3

    # Define the number of cars that have passed the halfway point
    halfway_cars = cars // 2

    # Define the number of additional passengers after passing halfway point
    additional_passengers = 1

    # Calculate the total number of people at the end of the race
    total_people = initial_people + (halfway_cars * additional_passengers)

    # return the result
    result = total_people
    return result

print(solution())