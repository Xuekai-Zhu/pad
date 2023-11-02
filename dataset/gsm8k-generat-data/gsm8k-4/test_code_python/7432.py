def solution():
    """It takes 10 minutes to wash a car, 15 minutes to change oil, and 30 minutes to change a set of tires.  
    If mike washes 9 cars, changes the oil on 6 cars, and changes two sets of tires how many hours did he work?"""
    # Define the time it takes to wash a car, change oil, and change a set of tires in minutes
    CAR_WASH_TIME = 10
    OIL_CHANGE_TIME = 15
    TIRE_CHANGE_TIME = 30

    # Calculate the total time it takes to wash 9 cars
    total_car_wash_time = 9 * CAR_WASH_TIME

    # Calculate the total time it takes to change oil on 6 cars
    total_oil_change_time = 6 * OIL_CHANGE_TIME

    # Calculate the total time it takes to change 2 sets of tires
    total_tire_change_time = 2 * TIRE_CHANGE_TIME

    # Calculate the total time Mike worked in minutes
    total_time = total_car_wash_time + total_oil_change_time + total_tire_change_time

    # Convert the total time to hours
    hours_worked = total_time / 60

    result = hours_worked
    return result

print(solution())