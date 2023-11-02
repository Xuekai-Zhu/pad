def solution():
    nickels = 95 // 5  # Ray has 95 cents in nickels
    remaining_nickels = nickels - 5  # Ray gives 25 cents (5 nickels) to Peter
    
    # Ray gives twice as many cents to Randi as he gave to Peter
    cents_to_randi = 2 * 25  # Twice as many cents as given to Peter
    nickels_to_randi = cents_to_randi // 5  # Convert cents to nickels
    
    # Calculate the number of nickels Ray has left
    remaining_nickels -= nickels_to_randi
    
    result = remaining_nickels
    return result

print(solution())