def solution():
    # Calculate Jamison's weight
    mary_weight = 160
    jamison_weight = mary_weight + 20  # Mary weighs 20 lbs less than Jamison's weight
    john_weight = 1.25 * mary_weight  # John weighs one-quarter times more than what Mary weighs

    # Calculate the combined weight of the three
    total_weight = mary_weight + jamison_weight + john_weight
    result = total_weight
    return result

print(solution())