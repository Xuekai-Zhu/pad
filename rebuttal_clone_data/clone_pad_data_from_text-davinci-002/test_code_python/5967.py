def solution():
 
    pairs_knitted_1st_week = 12
    pairs_knitted_2nd_week = 12 + 4
    pairs_knitted_3rd_week = 12 + 4 + (12 + 4)/2
    pairs_knitted_4th_week = 12 + 4 + (12 + 4)/2 - 3
    total_pairs_knitted = pairs_knitted_1st_week + pairs_knitted_2nd_week + pairs_knitted_3rd_week + pairs_knitted_4th_week
    
    result = total_pairs_knitted
 
    return result

print(solution())