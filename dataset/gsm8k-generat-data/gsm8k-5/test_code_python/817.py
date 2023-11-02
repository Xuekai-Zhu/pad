def solution():
    daily_coffee_beans = 2 * 1.5  # Maddie uses 1.5 ounces of coffee beans per cup, and makes 2 cups per day
    weekly_coffee_beans = daily_coffee_beans * 7  # Maddie drinks coffee every day, so she needs to multiply by 7
    bags_of_coffee = weekly_coffee_beans / 10.5  # Each bag of coffee contains 10.5 ounces of beans
    cost_of_coffee = bags_of_coffee * 8  # Each bag of coffee costs $8
    cost_of_milk = 4 / 2  # Maddie uses 1/2 a gallon of milk, which costs $4 per gallon

    # Calculate the total cost of Maddie's coffee per week
    total_cost = cost_of_coffee + cost_of_milk
    result = total_cost
    return result

print(solution())