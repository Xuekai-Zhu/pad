def solution():
    """Dimitri eats 3 burgers per day. Each burger has a total of 20 calories. How many calories will he get after two days?"""
    # Define the number of burgers eaten per day and the number of days
    burgers_per_day = 3
    num_days = 2

    # Calculate the total number of burgers eaten
    total_burgers = burgers_per_day * num_days

    # Calculate the total number of calories consumed
    total_calories = total_burgers * 20

    # Display the total number of calories consumed
    result = total_calories
    return result

print(solution())