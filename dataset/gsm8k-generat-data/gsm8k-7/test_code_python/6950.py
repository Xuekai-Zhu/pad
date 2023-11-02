def solution():
    total_earnings = 85
    ratio = 4
    # Let L be the amount Lottie earned
    L = total_earnings / (ratio + 1)
    # Jerusha earned 4 times as much money as Lottie
    J = ratio * L
    result = J
    return result

print(solution())