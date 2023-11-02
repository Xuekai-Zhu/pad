def solution():
    
    initial_milk = 30000
    pumped_out = 2880 * 4
    added_back = 1500 * 7
    remaining_milk = initial_milk - pumped_out + added_back
    result = remaining_milk
    return result

print(solution())