def solution():
    """A Tyrannosaurus rex ate half of a small triceratops it had hunted. When it left, a pack of velociraptors scavenged half of what was left. A group of lazy Allosaurus gulped down the last 270 kilograms of meat. How many kilograms of meat were on the triceratops before the T-Rex ate?"""
    final_weight = 270
    remaining_weight_1 = final_weight * 2
    remaining_weight_2 = remaining_weight_1 * 2
    initial_weight = remaining_weight_2 * 2
    result = initial_weight
    return result

print(solution())