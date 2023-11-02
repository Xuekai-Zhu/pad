def solution():
    """Three adults whose average weight is 140 pounds went first in the elevator. Two children whose average weight is 64 pounds also went inside. If an elevator sign reads “Maximum weight 600 pounds.", what is the maximum weight of the next person to get in the elevator so that it will not be overloaded?"""
    adults_weight = 140
    children_weight = 64
    max_weight = 600
    current_weight = 3 * adults_weight + 2 * children_weight
    remaining_weight = max_weight - current_weight
    result = remaining_weight
    return result

print(solution())