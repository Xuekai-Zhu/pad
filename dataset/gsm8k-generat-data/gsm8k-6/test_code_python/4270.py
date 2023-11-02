def solution():
    # Calculate the weight of five regular dinosaurs combined
    regular_weight = 5 * 800

    # Calculate Barney's weight
    barney_weight = regular_weight + 1500

    # Calculate the combined weight of Barney and the five regular dinosaurs
    total_weight = regular_weight + barney_weight
    result = total_weight
    return result

print(solution())