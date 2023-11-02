def solution():
    
    total_tomatoes = 127
    eaten_tomatoes = 19
    harvested_tomatoes = total_tomatoes - eaten_tomatoes
    given_tomatoes = harvested_tomatoes / 2
    remaining_tomatoes = harvested_tomatoes - given_tomatoes
    result = remaining_tomatoes
    return result

print(solution())