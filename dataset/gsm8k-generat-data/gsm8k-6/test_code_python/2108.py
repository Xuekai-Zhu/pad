def solution():
    # Calculate the total number of apples Adam bought in three days
    monday_apples = 15
    tuesday_apples = 3 * monday_apples
    wednesday_apples = 4 * tuesday_apples
    total_apples = monday_apples + tuesday_apples + wednesday_apples
    result = total_apples
    return result

print(solution())