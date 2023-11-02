def solution():
    
    cases = 10
    bottles_per_case = 20
    total_bottles = cases * bottles_per_case
    bottles_used = 70
    bottles_remaining = 20
    bottles_used_second_game = total_bottles - bottles_remaining - bottles_used
    result = bottles_used_second_game
    return result

print(solution())