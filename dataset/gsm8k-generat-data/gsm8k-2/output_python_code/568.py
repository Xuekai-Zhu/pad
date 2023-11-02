def solution():
    """At a gym, the blue weights are 2 pounds each, and the green weights are 3 pounds each. Harry put 4 blue weights and 5 green weights onto a metal bar. The bar itself weighs 2 pounds. What is the total amount of weight, in pounds, of Harry's custom creation?"""
    blue_weight = 2
    green_weight = 3
    metal_bar_weight = 2
    blue_total_weight = 4 * blue_weight
    green_total_weight = 5 * green_weight
    total_weight = blue_total_weight + green_total_weight + metal_bar_weight
    result = total_weight
    return result

print(solution())