def solution():
    # Calculate the total amount of coffee beans Maddie uses per week
    coffee_beans_per_cup = 1.5
    cups_of_coffee_per_day = 2
    total_coffee_beans_used_per_week = coffee_beans_per_cup * cups_of_coffee_per_day * 7

    # Calculate the total cost of coffee Maddie uses per week
    ounces_of_coffee_in_one_bag = 10.5
    cost_of_one_bag_of_coffee = 8
    total_cost_of_coffee_per_week = (total_coffee_beans_used_per_week / ounces_of_coffee_in_one_bag) * cost_of_one_bag_of_coffee

    # Calculate the total cost of milk Maddie uses per week
    gallons_of_milk_per_week = 0.5
    cost_of_one_gallon_of_milk = 4
    total_cost_of_milk_per_week = gallons_of_milk_per_week * cost_of_one_gallon_of_milk

    # Calculate the total cost of Maddie's coffee per week
    total_cost_of_coffee_per_week = total_cost_of_coffee_per_week + total_cost_of_milk_per_week

    result = total_cost_of_coffee_per_week
    return result

print(solution())