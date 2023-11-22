def solution():
    
    # Define the number of cars counted during the first break
    cars_first_break = 50

    # Define the number of cars counted during the second break
    cars_second_break = 20

    # Calculate the number of cars counted during the lunch break
    cars_lunch_break = cars_first_break + (1/2) * cars_second_break

    # Display the total number of cars counted during lunch break
    result = cars_lunch_break
    return result

print(solution())