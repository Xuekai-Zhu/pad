def solution():
    
    quarters = 20
    nickel_value = 0.05
    iron_nickel_percentage = 0.2
    iron_nickel_value = 3
    nickels = quarters * 5
    iron_nickels = int(nickels * iron_nickel_percentage)
    regular_nickels = nickels - iron_nickels
    total_value = regular_nickels * nickel_value + iron_nickels * iron_nickel_value
    result = total_value
    return result

print(solution())