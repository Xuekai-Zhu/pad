def solution():
    # Calculate the number of girls at the camp
    girls = 40 * 3
    
    # Calculate the total number of children at the camp
    children = girls + 40
    
    # Calculate the number of counselors needed
    counselors = children // 8
    
    result = counselors
    return result

print(solution())