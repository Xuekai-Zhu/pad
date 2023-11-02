def solution():
    # Calculate the number of visitors who fell ill
    ill_visitors = 0.4 * 500

    # Calculate the number of visitors who did not fall ill
    healthy_visitors = 500 - ill_visitors
    result = healthy_visitors
    return result

print(solution())