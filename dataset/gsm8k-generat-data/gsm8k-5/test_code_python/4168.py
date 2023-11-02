def solution():
    jimmy_weight = 75 + 6  # Jimmy weighs 6 pounds more than Rachel
    adam_weight = 75 - 15  # Adam weighs 15 pounds less than Rachel

    # Calculate the total weight of the three people
    total_weight = rachel_weight + jimmy_weight + adam_weight

    # Calculate the average weight
    average_weight = total_weight / 3
    result = average_weight
    return result

print(solution())