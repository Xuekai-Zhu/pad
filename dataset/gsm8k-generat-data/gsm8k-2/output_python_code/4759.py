def solution():
    """John weighs one-quarter times more than what Mary weighs. Mary weighs 20 lbs less than Jamison's weight. If Mary weighs 160 lbs, what's the combined weight of the three?"""
    mary_weight = 160
    jamison_weight = mary_weight + 20
    john_weight = 1.25 * mary_weight
    total_weight = mary_weight + jamison_weight + john_weight
    result = total_weight
    return result

print(solution())