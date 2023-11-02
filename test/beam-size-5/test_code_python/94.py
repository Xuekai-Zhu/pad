def solution():
    
    # Define the total number of cars on the motorway
    total_cars = 30

    # Calculate the number of cars who drive through the traffic jam in the first 15 minutes
    first_15_min_cars = total_cars - 15

    # Calculate the number of cars who drive through the traffic jam in the remaining 15 minutes
    remaining_15_min_cars = 20

    # Calculate the number of cars who drive through the traffic jam in the remaining 15 minutes
    remaining_15_min_cars = remaining_15_min_cars + 5

    # Calculate the number of cars who drive through the traffic jam in the first 15 minutes
    first_15_min_cars = first_15_min_cars + remaining_15_min_cars

    # Display the number of cars who drive through the traffic jam in the first 15 minutes
    result = first_15_min_cars
    return result

print(solution())