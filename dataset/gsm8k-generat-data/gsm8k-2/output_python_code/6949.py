def solution():
    """Jerusha earned 4 times as much money as Lottie. Together they earned $85. How many dollars did Jerusha earn? Use L to represent Lottie's earnings."""
    total_earnings = 85
    j_ratio = 4
    l_earnings = total_earnings / (j_ratio + 1)
    j_earnings = j_ratio * l_earnings
    result = j_earnings
    return result

print(solution())