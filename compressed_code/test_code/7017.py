def solution():
    
    matthews_cows = 60
    aaron_cows = 4 * matthews_cows
    marovich_cows = aaron_cows + matthews_cows - 30
    total_cows = matthews_cows + aaron_cows + marovich_cows
    result = total_cows
    return result

print(solution())