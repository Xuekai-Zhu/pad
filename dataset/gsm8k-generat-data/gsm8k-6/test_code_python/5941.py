def solution():
    morning_milk = 365  # gallons of milk this morning
    evening_milk = 380  # gallons of milk this evening
    sold_milk = 612  # gallons of milk sold to the ice cream factory
    leftover_milk = 15  # gallons of milk left over from yesterday
    
    # Calculate the total milk Aunt May has left
    total_milk = morning_milk + evening_milk + leftover_milk - sold_milk
    result = total_milk
    return result

print(solution())