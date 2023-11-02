def solution():
    
    monday_visited = 32
    tuesday_visited = monday_visited * 2
    wednesday_visited = tuesday_visited * 3
    thursday_visited = 30
    friday_visited = 25
    total_visited = monday_visited + tuesday_visited + wednesday_visited + thursday_visited + friday_visited
    result = total_visited
    return result

print(solution())