def solution():
    quarters_per_pile = 10  # Rocco has 10 quarters in each pile
    dimes_per_pile = 10  # Rocco has 10 dimes in each pile
    nickels_per_pile = 10  # Rocco has 10 nickels in each pile
    pennies_per_pile = 10  # Rocco has 10 pennies in each pile
    
    # Calculate the total value of each type of coin
    total_quarters_value = 4 * quarters_per_pile * 0.25  # Rocco has 4 piles of quarters
    total_dimes_value = 6 * dimes_per_pile * 0.1  # Rocco has 6 piles of dimes
    total_nickels_value = 9 * nickels_per_pile * 0.05  # Rocco has 9 piles of nickels
    total_pennies_value = 5 * pennies_per_pile * 0.01  # Rocco has 5 piles of pennies
    
    # Calculate the total value of all of Rocco's coins
    total_value = total_quarters_value + total_dimes_value + total_nickels_value + total_pennies_value
    result = total_value
    return result

print(solution())