def solution():
    # Calculate the total cost of the light bulbs
    total_cost = 3*8 + 1*12  # 3 small bulbs cost $8 each and 1 large bulb costs $12
    
    # Calculate the amount of money Valerie will have left over
    money_left = 60 - total_cost
    
    result = money_left
    return result

print(solution())