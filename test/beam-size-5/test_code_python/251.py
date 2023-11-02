def solution():
    # Calculate the total number of cows in the stalls
    total_cows = 10 * 20

    # Divide the cows equally among the 20 stalls
    cows_each = total_cows // 20

    # Calculate the total number of cows in 8 stalls
    total_cows_8_stalls = 8 * cows_each

    result = total_cows_8_stalls
    return result

print(solution())