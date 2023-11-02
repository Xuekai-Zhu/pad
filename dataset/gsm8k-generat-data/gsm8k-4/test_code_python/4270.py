def solution():
    """Barney the dinosaur weighs 1500 pounds more than five regular dinosaurs combined. If each regular dinosaur weighs 800 pounds, find the combined weight of Barney and the five regular dinosaurs' weights?"""
    # Calculate the weight of five regular dinosaurs combined
    regular_dinosaurs_weight = 5 * 800

    # Calculate Barney's weight
    barney_weight = regular_dinosaurs_weight + 1500

    # Calculate the combined weight
    combined_weight = barney_weight + regular_dinosaurs_weight

    result = combined_weight
    return result

print(solution())