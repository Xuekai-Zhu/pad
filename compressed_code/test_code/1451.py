def solution():
    
    initial_dimes = 2
    initial_quarters = 6
    initial_nickels = 5
    added_dimes = 2
    added_quarters = 10
    added_nickels = 2 * initial_nickels
    total_coins = initial_dimes + initial_quarters + initial_nickels + added_dimes + added_quarters + added_nickels
    result = total_coins
    return result

print(solution())