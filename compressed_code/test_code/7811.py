def solution():
    
    small_apple_cost = 1.5
    medium_apple_cost = 2
    big_apple_cost = 3
    small_and_medium_apples = 6
    big_apples = 8
    
    total_cost = (small_and_medium_apples * (small_apple_cost + medium_apple_cost)
                  + big_apples * big_apple_cost)
    result = total_cost
    return result

print(solution())