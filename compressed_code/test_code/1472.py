def solution():
    
    monday_distance = 40
    tuesday_distance = 50
    wednesday_distance = 0.5 * tuesday_distance
    thursday_distance = monday_distance + wednesday_distance
    total_distance = monday_distance + tuesday_distance + wednesday_distance + thursday_distance
    result = total_distance
    return result

print(solution())