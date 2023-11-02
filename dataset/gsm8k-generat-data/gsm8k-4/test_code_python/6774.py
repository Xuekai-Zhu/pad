def solution():
    """At a certain car dealership, 15% of the cars cost less than $15000 and 40% of the cars cost more than $20000. If there are 3000 cars at the dealership, how many of them cost between $15000 and $20000?"""
    # Define the total number of cars
    total_cars = 3000

    # Calculate the number of cars that cost less than $15000
    less_than_15k_cars = total_cars * 0.15

    # Calculate the number of cars that cost more than $20000
    more_than_20k_cars = total_cars * 0.4

    # Calculate the number of cars that cost between $15000 and $20000
    between_15k_and_20k_cars = total_cars - less_than_15k_cars - more_than_20k_cars

    # Return the result
    result = between_15k_and_20k_cars
    return result

print(solution())