def solution():
    
    num_regular_dinosaurs = 5
    weight_regular_dinosaur = 800
    total_weight_regular_dinosaurs = num_regular_dinosaurs * weight_regular_dinosaur
    weight_barney = total_weight_regular_dinosaurs + 1500
    total_weight = total_weight_regular_dinosaurs + weight_barney
    result = total_weight
    return result

print(solution())