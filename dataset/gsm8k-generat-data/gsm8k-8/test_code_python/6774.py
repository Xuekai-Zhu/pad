def solution():
    # Define the total number of cars and the percentages of cars in different price ranges
    total_cars = 3000
    less_than_15000_percent = 0.15
    more_than_20000_percent = 0.4

    # Calculate the number of cars in each price range
    less_than_15000_cars = total_cars * less_than_15000_percent
    more_than_20000_cars = total_cars * more_than_20000_percent
    other_cars = total_cars - less_than_15000_cars - more_than_20000_cars

    # Calculate the number of cars that cost between $15000 and $20000
    between_15000_and_20000_cars = other_cars
    result = between_15000_and_20000_cars
    return result

print(solution())