def solution():
    # Find the combined weight of the five regular dinosaurs
    regular_dinosaur_weight = 800
    combined_regular_weight = 5 * regular_dinosaur_weight

    # Find Barney's weight
    barney_weight = combined_regular_weight + 1500

    # Find the combined weight of all dinosaurs
    total_weight = combined_regular_weight + barney_weight
    result = total_weight
    return result

print(solution())