def solution():
    """Steve is holding nickels and dimes in his hand. He has 4 more dimes than nickels. He has a total of 70 cents in his hand. How many nickels is he holding?"""
    total_value = 70
    nickel_value = 5
    dime_value = 10
    dime_count = 0
    nickel_count = 0
    
    # loop through all possible counts of nickels and dimes to find a valid combination
    for i in range(total_value // nickel_value + 1):
        nickel_count = i
        dime_count = i + 4
        if (nickel_count * nickel_value) + (dime_count * dime_value) == total_value:
            break
    
    result = nickel_count
    return result

print(solution())