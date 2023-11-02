def solution():
    
    scarves_per_yarn = 3
    total_red_yarns = 2
    total_blue_yarns = 6
    total_yellow_yarns = 4
    total_yarns = total_red_yarns + total_blue_yarns + total_yellow_yarns
    total_scarves = total_yarns * scarves_per_yarn
    result = total_scarves
    return result

print(solution())