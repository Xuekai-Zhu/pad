def solution():
    bed_frame_cost = 75
    bed_cost = bed_frame_cost * 10
    percent_off = 20
    total_cost = bed_cost + bed_frame_cost
    discount = total_cost * (percent_off / 100)
    final_cost = total_cost - discount
    result = final_cost
    
    return result

print(solution())