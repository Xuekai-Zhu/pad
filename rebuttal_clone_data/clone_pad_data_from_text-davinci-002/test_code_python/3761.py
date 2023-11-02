def solution():
    fleas_left = 14
    fleas_ treated = 4
    fleas_before = fleas_left * 2**fleas_treated
    result = fleas_before - fleas_left
    return result

print(solution())