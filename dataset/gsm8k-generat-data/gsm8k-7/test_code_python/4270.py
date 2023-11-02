def solution():
    weight_of_regular_dinosaur = 800
    num_regular_dinosaurs = 5
    
    # Calculate the total weight of the five regular dinosaurs
    total_regular_dinosaur_weight = weight_of_regular_dinosaur * num_regular_dinosaurs
    
    # Calculate the weight of Barney
    weight_of_barney = total_regular_dinosaur_weight + 1500
    
    # Calculate the combined weight of Barney and the five regular dinosaurs
    combined_weight = weight_of_barney + total_regular_dinosaur_weight
    
    result = combined_weight
    return result

print(solution())