def solution():
    jimmy_weight = 75 + 6  # Jimmy weighs 6 pounds more than Rachel
    adam_weight = 75 - 15  # Adam weighs 15 pounds less than Rachel

    # Calculate the total weight of all three people
    total_weight = jimmy_weight + adam_weight + 75

    # Calculate the average weight of the three people
    avg_weight = total_weight / 3
    result = avg_weight
    return result

print(solution())