def solution():
    """Cars have lined up on the motorway. Some of the cars drive through in the first 15 minutes of the traffic jam, then 20 more cars drive through in the remaining 15 minutes of the jam. 5 cars from the line take an exit so they don't have to drive through the traffic jam. If there were originally 30 cars on the motorway, how many cars drove through the traffic jam in the first 15 minutes?"""
    total_cars = 30
    cars_exiting = 5
    cars_remaining = total_cars - cars_exiting
    cars_first_15 = cars_remaining - 20
    result = cars_first_15
    return result

print(solution())