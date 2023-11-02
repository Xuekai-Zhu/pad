def solution():
    """Barney the dinosaur weighs 1500 pounds more than five regular dinosaurs combined. If each regular dinosaur weighs 800 pounds, find the combined weight of Barney and the five regular dinosaurs' weights?"""
    # Define the weight of each regular dinosaur
    REGULAR_DINOSAUR_WEIGHT = 800

    # Calculate the weight of five regular dinosaurs combined
    combined_regular_weight = 5 * REGULAR_DINOSAUR_WEIGHT

    # Calculate Barney's weight
    barney_weight = combined_regular_weight + 1500

    # Calculate the total weight
    total_weight = barney_weight + combined_regular_weight

    # Display the total weight
    result = total_weight
    return result

print(solution())