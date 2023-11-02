def solution():
    
    chairs = 18
    tables = 6
    stools = 4
    sticks_per_chair = 6
    sticks_per_table = 9
    sticks_per_stool = 2
    sticks = (chairs * sticks_per_chair) + (tables * sticks_per_table) + (stools * sticks_per_stool)
    hours = sticks / 5
    result = hours
    return result

print(solution())