def solution():
    matthews_cows = 60
    aaron_cows = 4 * matthews_cows
    marovich_cows = (matthews_cows + aaron_cows) - 30

    # Calculate the total number of cows
    total_cows = matthews_cows + aaron_cows + marovich_cows
    result = total_cows
    return result

print(solution())