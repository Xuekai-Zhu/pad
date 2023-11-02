def solution():
    
    bath_time = 20
    dry_time = bath_time / 2
    walk_distance = 3
    walk_speed = 6
    walk_time = walk_distance / walk_speed
    total_time = bath_time + dry_time + walk_time * 60
    result = total_time
    return result

print(solution())