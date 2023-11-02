def solution():
    # Calculate the total weight of the pie
    total_weight = 1200 / (1 - 1/6)

    # Calculate the weight that Sophia ate
    sophia_ate = total_weight * 1/6
    result = sophia_ate
    return result

print(solution())