def solution():
    # Define the total number of cars and the number of Chevys
    total_cars = 301
    chevy_num = x

    # Calculate the number of Fords and Buicks
    ford_num = (2 * chevy_num) + 3
    buick_num = 4 * ford_num

    # Calculate the total number of cars
    total_num = chevy_num + ford_num + buick_num

    # Solve for Chevy number using total equation
    chevy_num = total_cars - (4*(2*(total_cars-3)/13)) - (4*(total_cars-3)/13) - 3

    result = buick_num
    return result

print(solution())