def solution():
    monday_lunch = 3
    monday_dinner = monday_lunch * 2
    tuesday_breakfast = 1

    monday_total = monday_lunch + monday_dinner
    tuesday_total = tuesday_breakfast

    diff = monday_total - tuesday_total
    result = diff
    return result

print(solution())