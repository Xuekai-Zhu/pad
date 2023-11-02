def solution():
    # Calculate the total number of fries he can get from his potatoes
    total_fries = 25 * 15  # he can get 25 fries out of 1 potato, and he has 15 potatoes
    leftover_fries = total_fries - 200  # he needs 200 fries, so this is how many fries he will have left over
    leftover_potatoes = leftover_fries // 25  # each potato produces 25 fries, so divide by 25 to get the number of potatoes
    result = leftover_potatoes
    return result

print(solution())