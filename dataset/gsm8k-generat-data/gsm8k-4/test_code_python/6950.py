def solution():
    """Jerusha earned 4 times as much money as Lottie. Together they earned $85. How many dollars did Jerusha earn? Use L to represent Lottie's earnings."""
    # Let L be Lottie's earnings
    L = None

    # Jerusha earned 4 times as much as Lottie
    J = 4 * L

    # Together they earned $85
    total_earnings = L + J
    if total_earnings == 85:
        # Solve for L and J
        L = 17
        J = 68

    # Return Jerusha's earnings
    result = J
    return result

print(solution())