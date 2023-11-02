def solution():
    cups_per_day = 2
    ounces_per_cup = 1.5
    bag_cost = 8
    ounces_per_bag = 10.5
    milk_gallons_per_week = 0.5
    milk_cost_per_gallon = 4

    # Calculate the total ounces of coffee beans Maddie uses per week 
    ounces_per_week = cups_per_day * ounces_per_cup * 7

    # Calculate the total number of bags of coffee Maddie needs to buy per week
    bags_per_week = ounces_per_week / ounces_per_bag

    # Calculate the total cost of coffee per week
    coffee_cost_per_week = bags_per_week * bag_cost

    # Calculate the total cost of milk per week
    milk_cost_per_week = milk_gallons_per_week * milk_cost_per_gallon

    # Calculate the total cost of Maddie's coffee per week
    total_cost_per_week = coffee_cost_per_week + milk_cost_per_week
    result = total_cost_per_week
    return result

print(solution())