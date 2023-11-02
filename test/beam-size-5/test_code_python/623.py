def solution():
    
    # Define the number of cars pulled on the first three days
    first_three_days = 10 * 3

    # Define the number of cars pulled on the remaining days
    remaining_days = 7 - 4

    # Calculate the total number of cars pulled
    total_cars = first_three_days + remaining_days

    # Display the total number of cars pulled
    result = total_cars
    return result

print(solution())