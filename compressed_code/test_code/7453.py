def solution():
    
    monday_apple_count = 15
    tuesday_apple_count = monday_apple_count * 3
    wednesday_apple_count = tuesday_apple_count * 4
    total_apple_count = monday_apple_count + tuesday_apple_count + wednesday_apple_count
    result = total_apple_count
    return result

print(solution())