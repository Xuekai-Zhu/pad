def solution():
    """It takes 10 minutes to wash a car, 15 minutes to change oil, and 30 minutes to change a set of tires.  If mike washes 9 cars, changes the oil on 6 cars, and changes two sets of tires how many hours did he work?"""
    # Define the time it takes to do each task in minutes
    CAR_WASH_TIME = 10
    OIL_CHANGE_TIME = 15
    TIRE_CHANGE_TIME = 30

    # Define the number of cars that need each task
    wash_cars = 9
    oil_change_cars = 6
    tire_change_sets = 2

    # Calculate the total time in minutes
    total_time = (wash_cars * CAR_WASH_TIME) + (oil_change_cars * OIL_CHANGE_TIME) + (tire_change_sets * TIRE_CHANGE_TIME)

    # Convert the total time to hours
    hours_worked = total_time / 60

    # Display the hours worked
    result = hours_worked
    return result

print(solution())