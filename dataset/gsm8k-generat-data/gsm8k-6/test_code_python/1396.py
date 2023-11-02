def solution():
    morning_milk = 68  # gallons of milk yesterday morning
    evening_milk = 82  # gallons of milk yesterday evening
    this_morning_milk = morning_milk - 18 # gallons of milk this morning
    total_milk = morning_milk + evening_milk + this_morning_milk  # total gallons of milk
    sold_milk = total_milk - 24  # gallons of milk sold in the afternoon
    revenue = sold_milk * 3.50  # revenue from selling milk
    result = revenue
    return result

print(solution())