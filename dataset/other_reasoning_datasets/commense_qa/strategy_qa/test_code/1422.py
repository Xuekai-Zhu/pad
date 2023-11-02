def solution():
    peas_per_pod = 6
    pea_pods_needed = 20
    total_peas = peas_per_pod * pea_pods_needed
    squares_on_chessboard = 64
    if total_peas >= squares_on_chessboard:
        result = "yes"
    else:
        result = "no"
    return result

print(solution())