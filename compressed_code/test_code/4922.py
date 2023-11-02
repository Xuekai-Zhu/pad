def solution():
    
    hoop_height = 10 * 12 
    player_height = 6 * 12 
    required_reach = hoop_height + 6 
    arm_span = 22 
    total_reach = player_height + arm_span 
    required_jump_height = required_reach - total_reach 
    result = required_jump_height
    return result

print(solution())