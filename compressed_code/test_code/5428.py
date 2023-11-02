def solution():
    
    total_matchsticks = 50
    elvis_squares = 5
    ralph_squares = 3
    elvis_matchsticks = elvis_squares * 4
    ralph_matchsticks = ralph_squares * 8
    used_matchsticks = elvis_matchsticks + ralph_matchsticks
    remaining_matchsticks = total_matchsticks - used_matchsticks
    result = remaining_matchsticks
    return result

print(solution())