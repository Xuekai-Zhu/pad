def solution():
    height_of_hoop = 10
    minimum_reach = 6
    player_height = 6
    player_arm_reach = 22
    player_jump_reach = player_arm_reach - player_height
    necessary_jump_height = height_of_hoop + minimum_reach - player_jump_reach
    result = necessary_jump_height
    
    return result

print(solution())