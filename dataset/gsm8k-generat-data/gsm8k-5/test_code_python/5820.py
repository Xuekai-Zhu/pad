def solution():
    # Calculate the total number of bonnets made
    monday = 10
    tuesday_wednesday = 2 * monday
    thursday = monday + 5
    friday = thursday - 5
    total_bonnets = monday + tuesday_wednesday + thursday + friday

    # Calculate the number of bonnets sent to each orphanage
    bonnets_per_orphanage = total_bonnets / 5
    result = bonnets_per_orphanage
    return result

print(solution())