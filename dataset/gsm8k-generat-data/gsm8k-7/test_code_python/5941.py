def solution():
    morning_milk = 365
    evening_milk = 380
    sold_milk = 612
    leftover_milk = 15
    
    # Calculate the total amount of milk Aunt May has before selling any
    total_milk = morning_milk + evening_milk + leftover_milk
    
    # Calculate the amount of milk Aunt May has left after selling to the ice cream factory
    remaining_milk = total_milk - sold_milk
    
    result = remaining_milk
    return result

print(solution())