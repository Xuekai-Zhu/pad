def solution():
    monday_bonnets = 10
    tuesday_wednesday_bonnets = monday_bonnets * 2
    thursday_bonnets = monday_bonnets + 5
    friday_bonnets = thursday_bonnets - 5

    total_bonnets = monday_bonnets + tuesday_wednesday_bonnets + thursday_bonnets + friday_bonnets

    num_orphanages = 5
    bonnets_per_orphanage = total_bonnets // num_orphanages
    result = bonnets_per_orphanage
    return result

print(solution())