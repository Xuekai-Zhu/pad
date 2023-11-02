def solution():
    num_zebras = 12
    
    # Calculate the number of camels
    num_camels = num_zebras / 2
    
    # Calculate the number of monkeys
    num_monkeys = num_camels * 4
    
    # Calculate the difference between the number of monkeys and giraffes
    num_giraffes = 2
    diff_monkeys_giraffes = num_monkeys - num_giraffes
    
    result = diff_monkeys_giraffes
    return result

print(solution())