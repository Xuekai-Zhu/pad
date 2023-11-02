def solution():
    cups_per_day = 2
    days_per_week = 7
    ounces_per_cup = 1.5
    price_per_bag = 8
    ounces_per_bag = 10.5
    gallons_per_week = 1/2
    price_per_gallon = 4
    price_per_ounce_coffee = price_per_bag / ounces_per_bag
    price_per_cup_coffee = price_per_ounce_coffee * ounces_per_cup
    price_per_week_coffee = price_per_cup_coffee * cups_per_day * days_per_week
    price_per_gallon_milk = price_per_gallon / gallons_per_week
    total_price_coffee = price_per_week_coffee + price_per_gallon_milk
    result = total_price_coffee
    
    return result

print(solution())