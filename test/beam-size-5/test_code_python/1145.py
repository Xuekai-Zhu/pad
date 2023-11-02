def solution():
    num_fish = 3
    food_per_fish_per_day = 1
    days_per_month = 31

    # Calculate the total amount of food needed for one day
    total_food_per_day = num_fish * food_per_fish_per_day

    # Calculate the total amount of food needed for one month
    total_food_per_month = total_food_per_day * days_per_month

    result = total_food_per_month
    return result

print(solution())