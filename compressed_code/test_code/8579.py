def solution():
    
    bottles_per_dozen = 12
    initial_bottles = 4 * bottles_per_dozen
    bottles_taken_first_break = 11 * 2
    bottles_taken_end_game = 11 * 1
    remaining_bottles = initial_bottles - bottles_taken_first_break - bottles_taken_end_game
    result = remaining_bottles
    return result

print(solution())