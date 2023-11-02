def solution():
    
    
    bath_time = 20 
    blow_dry_time = bath_time / 2 
    walk_distance = 3 
    walk_speed = 6 
    
    
    walk_time = (walk_distance / walk_speed) * 60
    total_time = bath_time + blow_dry_time + walk_time
    
    return total_time

print(solution())