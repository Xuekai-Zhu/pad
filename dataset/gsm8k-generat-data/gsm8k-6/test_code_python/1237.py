def solution():
    # Calculate the amount raised by washing 5 SUVs and 5 trucks
    total_SUV = 5 * 7
    total_truck = 5 * 6
    total_raised = total_SUV + total_truck

    # Calculate the number of cars washed
    num_cars = (100 - total_raised) / 5

    result = num_cars
    return result

print(solution())