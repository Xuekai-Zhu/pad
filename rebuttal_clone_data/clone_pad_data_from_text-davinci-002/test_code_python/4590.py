def solution():
    pomelos_per_box = 240
    boxes_shipped_1 = 10
    boxes_shipped_2 = 20
    total_pomelos = pomelos_per_box * boxes_shipped_1 + pomelos_per_box * boxes_shipped_2
    dozens_per_pomelo = 12
    total_dozens = total_pomelos / dozens_per_pomelo
    result = total_dozens
    return result

print(solution())