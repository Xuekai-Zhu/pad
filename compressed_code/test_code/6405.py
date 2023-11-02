def solution():
    
    monday_lunch = 3
    monday_dinner = monday_lunch * 2
    monday_total = monday_lunch + monday_dinner
    tuesday_breakfast = 1
    tuesday_total = tuesday_breakfast
    difference = monday_total - tuesday_total
    result = difference
    return result

print(solution())