def solution():
    """Maddie wants to see how much her mom spends on coffee each week. She makes herself 2 cups of coffee per day. Each cup has 1.5 ounces of coffee beans. A bag of coffee costs $8 and contains 10.5 ounces of beans. She uses 1/2 a gallon of milk per week. A gallon of milk costs $4. She doesn't add any sugar to the coffee. How much does she spend on her coffee per week?"""
    cups_per_day = 2
    ounces_per_cup = 1.5
    ounces_per_bag = 10.5
    bag_cost = 8
    milk_per_week = 0.5
    milk_cost_per_gallon = 4

    total_ounces = cups_per_day * 7 * ounces_per_cup
    bags_needed = total_ounces / ounces_per_bag
    total_cost_for_coffee = bags_needed * bag_cost
    total_cost_for_milk = milk_per_week * milk_cost_per_gallon
    total_cost = total_cost_for_coffee + total_cost_for_milk
    result = total_cost
    return result

print(solution())