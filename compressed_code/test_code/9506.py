def solution():
    
    total_apples = 20
    monday_apples = 2
    friday_apples = monday_apples / 2
    thursday_apples = 4 * friday_apples
    tuesday_apples = 2 * monday_apples
    wednesday_apples = total_apples - monday_apples - tuesday_apples - thursday_apples - friday_apples
    result = wednesday_apples
    return result

print(solution())