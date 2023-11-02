def solution():
     monday_distance = 40
     tuesday_distance = 50
     wednesday_distance = tuesday_distance / 2
     thursday_distance = monday_distance + wednesday_distance
     total_distance = monday_distance + tuesday_distance + wednesday_distance + thursday_distance
     return total_distance

print(solution())