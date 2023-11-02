def solution():
    
    monday_bonnets = 10
    tuesday_wednesday_bonnets = 2 * monday_bonnets
    thursday_bonnets = monday_bonnets + 5
    friday_bonnets = thursday_bonnets - 5
    total_bonnets = monday_bonnets + tuesday_wednesday_bonnets + thursday_bonnets + friday_bonnets
    bonnets_per_orphanage = total_bonnets / 5
    result = bonnets_per_orphanage
    return result

print(solution())