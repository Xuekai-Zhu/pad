def solution():
    
    initial_milk = 30000
    pumped_milk = 2880 * 4
    added_milk = 1500 * 7
    remaining_milk = initial_milk - pumped_milk + added_milk
    result = remaining_milk
    return result

print(solution())