def solution():
    
    # Define the fuel efficiency in miles per gallon
    fuel_efficiency = 10

    # Define the current price in regular gas
    regular_price = 3

    # Define the distance between Andy's home and office in miles
    distance = 5

    # Calculate the total distance traveled in a week
    weekly_distance = 2 * distance

    # Calculate the total cost of the fuel efficiency in a week
    fuel_cost = weekly_distance * fuel_efficiency

    # Calculate the total cost of the car for the week
    car_cost = fuel_cost * 4

    # return the result
    result = car_cost
    return result

print(solution())