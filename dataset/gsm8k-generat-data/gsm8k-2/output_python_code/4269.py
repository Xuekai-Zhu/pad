def solution():
    """Barney the dinosaur weighs 1500 pounds more than five regular dinosaurs combined. If each regular dinosaur weighs
    800 pounds, find the combined weight of Barney and the five regular dinosaurs' weights?"""
    regular_dino_weight = 800
    total_regular_dino_weight = 5 * regular_dino_weight
    barney_weight = total_regular_dino_weight + 1500
    combined_weight = barney_weight + total_regular_dino_weight
    result = combined_weight
    return result

print(solution())