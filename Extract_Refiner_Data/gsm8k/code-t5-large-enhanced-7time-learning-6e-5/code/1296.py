def solution():
    
    # Define the number of cars Josh services per day
    CARS_PER_DAY = 3

    # Define the number of days in a week
    DAYS_PER_WEEK = 7 - 2  # Subtract Sunday and Wednesday

    # Define the number of weeks Josh wants to know how much he makes in 2 weeks
    WEEKS = 2

    # Calculate the total number of cars Josh services in 2 weeks
    total_cars = CARS_PER_DAY * DAYS_PER_WEEK * WEEKS

    # Calculate the total amount of money Josh makes in 2 weeks
    total_money = total_cars * 4

    # Display the total amount of money Josh makes in 2 weeks
    result = total_money
    return result

print(solution())