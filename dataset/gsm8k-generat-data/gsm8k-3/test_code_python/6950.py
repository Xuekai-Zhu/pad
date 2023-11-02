def solution():
    """Jerusha earned 4 times as much money as Lottie. Together they earned $85. How many dollars did Jerusha earn? Use L to represent Lottie's earnings."""
    # Let L represent Lottie's earnings
    L = 1

    # Jerusha earned 4 times as much as Lottie
    J = 4 * L

    # Together they earned $85
    total_earnings = J + L
    while total_earnings != 85:
        L += 1
        J = 4 * L
        total_earnings = J + L

    # Display Jerusha's earnings
    result = J
    return result

print(solution())