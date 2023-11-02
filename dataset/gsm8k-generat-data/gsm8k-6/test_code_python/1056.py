def solution():
    # Calculate the number of carrots needed
    carrots = 6 * 2  # 6 times as many carrots as potatoes
    
    # Calculate the number of onions needed
    onions = 2 * carrots  # twice as many onions as carrots
    
    # Calculate the number of green beans needed
    green_beans = int(1/3 * onions)  # 1/3 as many green beans as onions
    
    result = green_beans
    return result

print(solution())