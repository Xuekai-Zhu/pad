def solution():
    
    initial_pencils = 30
    lost_pencils = 6
    remaining_pencils = initial_pencils - lost_pencils
    lost_again_pencils = remaining_pencils / 3
    current_pencils = remaining_pencils - lost_again_pencils
    result = current_pencils
    return result

print(solution())