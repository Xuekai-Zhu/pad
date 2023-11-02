def solution():
    total_hours = 3
    leaves_1st_hour = 7
    leaves_2nd_hour = 4
    leaves_3rd_hour = 4
    total_leaves = leaves_1st_hour + leaves_2nd_hour + leaves_3rd_hour
    average_leaves = total_leaves / total_hours
    result = average_leaves
    
    return result

print(solution())