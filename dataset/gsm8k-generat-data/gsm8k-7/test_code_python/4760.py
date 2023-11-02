def solution():
    mary_weight = 160
    jamison_weight = mary_weight + 20
    john_weight = 1.25 * mary_weight     # John weighs one-quarter times more than Mary

    # Calculate the combined weight of Mary, Jamison, and John
    total_weight = mary_weight + jamison_weight + john_weight
    result = total_weight
    return result

print(solution())