def solution():
    """There are 96 fourth-graders at Small Tree School. 43 of them are girls. On Friday, 5 fourth-grade girls and 4 fourth-grade boys were absent. How many fourth grade boys were at Small Tree School on Friday?"""
    total_students = 96
    girls = 43
    absent_girls = 5
    absent_boys = 4
    boys = total_students - girls
    boys_on_friday = boys - absent_boys
    result = boys_on_friday
    return result

print(solution())