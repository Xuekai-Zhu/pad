def solution():
    
    riverside_kids = 120
    west_side_kids = 90
    mountaintop_kids = 50
    denied_riverside = 0.2 * riverside_kids
    denied_west_side = 0.7 * west_side_kids
    denied_mountaintop = 0.5 * mountaintop_kids
    allowed_riverside = riverside_kids - denied_riverside
    allowed_west_side = west_side_kids - denied_west_side
    allowed_mountaintop = mountaintop_kids - denied_mountaintop
    total_allowed = allowed_riverside + allowed_west_side + allowed_mountaintop
    result = total_allowed
    return result

print(solution())