def solution():
    # Calculate the amount of coffee beans used per week
    coffee_beans_per_day = 2 * 1.5  # Maddie uses 2 cups of coffee per day, each cup has 1.5 ounces of coffee beans
    coffee_beans_per_week = 7 * coffee_beans_per_day

    # Calculate the number of bags of coffee needed per week
    bags_needed = coffee_beans_per_week / 10.5  # A bag of coffee contains 10.5 ounces of beans
    cost_of_coffee = bags_needed * 8  # The cost of one bag of coffee is $8

    # Calculate the cost of milk per week
    cost_of_milk = 0.5 * 4  # Maddie uses 1/2 gallon of milk per week, and a gallon of milk costs $4

    # Calculate the total cost of coffee per week
    total_cost = cost_of_coffee + cost_of_milk
    result = total_cost
    return result

print(solution())