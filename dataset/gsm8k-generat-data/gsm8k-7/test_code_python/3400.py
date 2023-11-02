def solution():
    roger_weight = 0
    ron_weight = 0
    combined_weight = 239

    # Calculate Ron's weight by using reverse iteration method
    for i in range(combined_weight, 0, -1):
        for j in range(i, 0, -1):
            for k in range(j, 0, -1):
                if i + j + k == combined_weight:
                    ron_weight = k

    # Calculate Roger's weight
    roger_weight = 4 * ron_weight - 7

    # Calculate Rodney's weight
    rodney_weight = 2 * roger_weight

    result = rodney_weight
    return result

print(solution())