def solution():
    """Maddie wants to see how much her mom spends on coffee each week. She makes herself 2 cups of coffee per day. Each cup has 1.5 ounces of coffee beans. A bag of coffee costs $8 and contains 10.5 ounces of beans. She uses 1/2 a gallon of milk per week. A gallon of milk costs $4. She doesn't add any sugar to the coffee. How much does she spend on her coffee per week?"""
    # Define the amount of coffee used per week
    coffee_used = 2 * 1.5 * 7

    # Calculate the number of bags of coffee needed per week
    bags_of_coffee = coffee_used / 10.5

    # Calculate the cost of the coffee beans per week
    cost_of_coffee = bags_of_coffee * 8

    # Calculate the cost of the milk per week
    cost_of_milk = 4 * 0.5

    # Calculate the total cost of Maddie's coffee per week
    total_cost = cost_of_coffee + cost_of_milk

    # return the result
    result = total_cost
    return result

print(solution())