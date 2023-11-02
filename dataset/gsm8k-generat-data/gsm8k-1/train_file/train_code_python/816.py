def solution():
    """Maddie wants to see how much her mom spends on coffee each week. She makes herself 2 cups of coffee per day. Each cup has 1.5 ounces of coffee beans. A bag of coffee costs $8 and contains 10.5 ounces of beans. She uses 1/2 a gallon of milk per week. A gallon of milk costs $4. She doesn't add any sugar to the coffee. How much does she spend on her coffee per week?"""
    cups_per_day = 2
    ounces_per_cup = 1.5
    bags_per_week = (cups_per_day * 7 * ounces_per_cup) / 10.5
    cost_per_bag = 8
    cost_per_week_on_coffee = bags_per_week * cost_per_bag
    gallons_per_week = 0.5
    cost_per_gallon = 4
    cost_per_week_on_milk = gallons_per_week * cost_per_gallon
    total_cost_per_week = cost_per_week_on_coffee + cost_per_week_on_milk
    result = total_cost_per_week
    return result

print(solution())