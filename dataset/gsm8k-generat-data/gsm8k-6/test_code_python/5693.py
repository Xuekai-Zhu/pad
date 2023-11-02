def solution():
    # Calculate the total number of sweaters Kim knit that week
    monday = 8
    tuesday = monday + 2
    wednesday = tuesday - 4
    thursday = wednesday - 4
    friday = monday / 2
    total_sweaters = monday + tuesday + wednesday + thursday + friday
    result = total_sweaters
    return result

print(solution())