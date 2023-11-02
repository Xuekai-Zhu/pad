def solution():
    
    starting_oranges = 5
    starting_tangerines = 17
    oranges_taken = 2
    tangerines_taken = 10
    remaining_oranges = starting_oranges - oranges_taken
    remaining_tangerines = starting_tangerines - tangerines_taken
    more_tangerines_than_oranges = remaining_tangerines - remaining_oranges
    result = more_tangerines_than_oranges
    return result

print(solution())