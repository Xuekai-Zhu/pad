def solution():
    # Calculate the total number of quarters Jenn has saved
    total_quarters = 5 * 160
    
    # Calculate the total amount of money Jenn has saved in dollars
    total_money = total_quarters * 0.25
    
    # Calculate the amount of money Jenn will have left over after buying the bike
    left_over_money = total_money - 180
    
    result = round(left_over_money, 2)  # round to two decimal places
    return result

print(solution())