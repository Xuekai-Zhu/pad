def solution():
    total_weight = 98
    ruperts_weight = (total_weight + 7) / 3  # Rupert's weight is one third of the total weight plus 7
    antoinettes_weight = (2 * ruperts_weight) - 7  # Antoinette's weight is twice Rupert's weight minus 7
    result = antoinettes_weight
    return result

print(solution())