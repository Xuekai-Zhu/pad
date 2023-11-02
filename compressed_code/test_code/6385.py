def solution():
    
    hour1_picked = 66
    hour2_picked = 2 * hour1_picked
    hour3_picked = hour1_picked / 3
    total_picked = hour1_picked + hour2_picked + hour3_picked
    result = total_picked
    return result

print(solution())