def solution():
    cars_per_group = 5
    trucks_per_group = 2 * cars_per_group
    
    num_cars = 6
    num_trucks = 3
    
    # Calculate the total number of people needed to lift all the cars
    cars_people_needed = num_cars * cars_per_group
    
    # Calculate the total number of people needed to lift all the trucks
    trucks_people_needed = num_trucks * trucks_per_group
    
    # Calculate the total number of people needed to lift all the vehicles
    total_people_needed = cars_people_needed + trucks_people_needed
    
    result = total_people_needed
    return result

print(solution())