def solution():
    # Define the initial investment
    initial_investment = 20 * 15
    
    # Calculate the new value of each coin after the increase
    new_value = 15 + (15 * 2/3)
    
    # Calculate the total value of all the coins after the increase
    total_value = 20 * new_value
    
    # Calculate the number of coins James needs to sell to recoup his initial investment
    coins_sold = initial_investment / new_value
    
    result = coins_sold
    
    return result

print(solution())