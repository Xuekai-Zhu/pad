def solution():
    # Calculate the total number of apples that Ella has
    total_apples = 4*20 + 6*25  # 4 bags with 20 apples in each and 6 bags with 25 apples in each
    remaining_apples = total_apples - 200 # Number of apples remaining after selling 200 apples
    result = remaining_apples
    return result

print(solution())