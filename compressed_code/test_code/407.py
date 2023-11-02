def solution():
    
    total_tomatoes = 18 * 7
    dried_tomatoes = total_tomatoes / 2
    remaining_tomatoes = total_tomatoes - dried_tomatoes
    marinara_tomatoes = remaining_tomatoes / 3
    remaining_tomatoes = remaining_tomatoes - marinara_tomatoes
    result = remaining_tomatoes
    return result

print(solution())