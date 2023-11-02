def solution():
    
    white_daisies = 6
    pink_daisies = 9 * white_daisies
    red_daisies = (4 * pink_daisies) - 3
    total_daisies = white_daisies + pink_daisies + red_daisies
    result = total_daisies
    return result

print(solution())