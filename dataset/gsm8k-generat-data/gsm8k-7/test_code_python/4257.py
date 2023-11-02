def solution():
    burgers_per_day = 3
    calories_per_burger = 20
    num_days = 2

    # Calculate the total number of burgers Dimitri will eat in two days
    total_burgers = burgers_per_day * num_days

    # Calculate the total number of calories Dimitri will get from all the burgers
    total_calories = total_burgers * calories_per_burger
    result = total_calories
    return result

print(solution())