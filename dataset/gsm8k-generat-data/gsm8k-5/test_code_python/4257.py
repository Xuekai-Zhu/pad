def solution():
    burgers_per_day = 3  # Dimitri eats 3 burgers per day
    calories_per_burger = 20  # Each burger has 20 calories
    days = 2  # Dimitri wants to know the total calories he will get after 2 days

    # Calculate the total number of burgers Dimitri will eat in 2 days
    total_burgers = burgers_per_day * days

    # Calculate the total number of calories Dimitri will consume
    total_calories = total_burgers * calories_per_burger
    result = total_calories
    return result

print(solution())