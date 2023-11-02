def solution():
    chairs = 18
    tables = 6
    stools = 4

    sticks_per_chair = 6
    sticks_per_table = 9
    sticks_per_stool = 2

    total_sticks = (chairs * sticks_per_chair) + (tables * sticks_per_table) + (stools * sticks_per_stool)

    sticks_per_hour = 5

    hours_of_heat = total_sticks / sticks_per_hour
    result = hours_of_heat
    return result

print(solution())