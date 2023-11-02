def solution():
    """Dimitri eats 3 burgers per day. Each burger has a total of 20 calories. How many calories will he get after two days?"""
    # Define the number of burgers and calories per burger
    burgers_per_day = 3
    calories_per_burger = 20

    # Calculate the total calories consumed after two days
    total_burgers = burgers_per_day * 2
    total_calories = total_burgers * calories_per_burger

    # Return the result
    result = total_calories
    return result

print(solution())