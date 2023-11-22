def solution():
    
    # Define the number of cars pulled on the first three days
    first_three_days_cars = 10 * 3

    # Define the number of cars pulled on the remaining days
    remaining_days_cars = 10 * 3 - 4 * 3

    # Calculate the total number of cars pulled
    total_cars = first_three_days_cars + remaining_days_cars

    # return the result
    result = total_cars
    return result

print(solution())