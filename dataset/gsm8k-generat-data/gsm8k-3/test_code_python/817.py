def solution():
    """Maddie wants to see how much her mom spends on coffee each week. She makes herself 2 cups of coffee per day. Each cup has 1.5 ounces of coffee beans. A bag of coffee costs $8 and contains 10.5 ounces of beans. She uses 1/2 a gallon of milk per week. A gallon of milk costs $4. She doesn't add any sugar to the coffee. How much does she spend on her coffee per week?"""
    # Find the amount of coffee beans Maddie uses per week
    coffee_beans_per_cup = 1.5/16 # convert ounces to pounds
    coffee_beans_per_week = coffee_beans_per_cup * 2 * 7 # 2 cups a day for 7 days

    # Calculate the number of bags of coffee Maddie needs to buy
    coffee_bags_per_week = coffee_beans_per_week / 10.5
    coffee_bags_per_week = math.ceil(coffee_bags_per_week) # round up to the nearest bag

    # Calculate the cost of the coffee bags Maddie needs to buy
    coffee_cost_per_week = coffee_bags_per_week * 8

    # Calculate the cost of the milk Maddie needs to buy
    milk_cost_per_week = 2 # 1/2 gallon of milk costs $4

    # Calculate the total cost of Maddie's coffee per week
    total_cost_per_week = coffee_cost_per_week + milk_cost_per_week

    # Display the total cost
    result = total_cost_per_week
    return result

print(solution())