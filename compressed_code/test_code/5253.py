def solution():
    
    starting_pencils = 20
    misplaced_pencils = 7
    broken_pencils = 3
    found_pencils = 4
    bought_pencils = 2
    remaining_pencils = starting_pencils - misplaced_pencils - broken_pencils + found_pencils + bought_pencils
    result = remaining_pencils
    return result

print(solution())