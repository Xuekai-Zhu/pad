def solution():
    
    # Define the number of cars and motorcycles
    num_cars = 57
    num_motos = 73

    # Define the number of wheels needed for each car and motorcycle
    car_wheels = 4
    motorcycle_wheels = 2

    # Calculate the total number of wheels needed
    total_wheels = (num_cars * car_wheels) + (num_motos * motorcycle_wheels)

    # Calculate the number of wheels left in the box
    wheels_left = 650 - total_wheels

    # Display the number of wheels left in the box
    result = wheels_left
    return result

print(solution())