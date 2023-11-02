def solution():
    regular_dinosaur_weight = 800  # Each regular dinosaur weighs 800 pounds
    total_regular_weight = regular_dinosaur_weight * 5  # The total weight of five regular dinosaurs
    barney_weight = total_regular_weight + 1500  # Barney weighs 1500 pounds more than the five regular dinosaurs combined
    
    # Calculate the combined weight of Barney and the five regular dinosaurs
    combined_weight = total_regular_weight + barney_weight
    result = combined_weight
    return result

print(solution())