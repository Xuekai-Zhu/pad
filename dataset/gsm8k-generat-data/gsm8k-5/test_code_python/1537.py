def solution():
    total_weight = 98  # Antoinette and Rupert weigh 98 kilograms in total

    # Let's assume Rupert weighs x kilograms
    # Therefore, Antoinette weighs 2x - 7 kilograms
    # Their weights in total will be x + 2x - 7 = 98
    # Solving for x, we get x = 35

    ruperts_weight = 35
    antoinettes_weight = 2 * ruperts_weight - 7
    result = antoinettes_weight
    return result

print(solution())