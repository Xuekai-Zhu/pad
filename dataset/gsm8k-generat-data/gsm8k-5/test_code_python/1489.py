def solution():
    # Calculate the weight lost by Seth, Jerome, and Veronica
    seth_weight_lost = 17.5
    jerome_weight_lost = 3 * seth_weight_lost
    veronica_weight_lost = seth_weight_lost + 1.5

    # Calculate the total weight lost by the three of them
    total_weight_lost = seth_weight_lost + jerome_weight_lost + veronica_weight_lost
    result = total_weight_lost
    return result

print(solution())