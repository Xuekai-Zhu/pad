def solution():
    """At a gym, the blue weights are 2 pounds each, and the green weights are 3 pounds each. Harry put 4 blue weights and 5 green weights onto a metal bar. The bar itself weighs 2 pounds. What is the total amount of weight, in pounds, of Harry's custom creation?"""
    blue_weight = 2
    green_weight = 3
    blue_weights_added = 4
    green_weights_added = 5
    bar_weight = 2
    total_weight = (blue_weight * blue_weights_added) + (green_weight * green_weights_added) + bar_weight
    result = total_weight
    return result

print(solution())