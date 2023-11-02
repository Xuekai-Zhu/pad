def solution():
    total_earnings = 85  # Jerusha and Lottie earned a total of $85
    earnings_ratio = 4  # Jerusha's earnings are 4 times Lottie's earnings
    total_parts = 1 + earnings_ratio  # Total number of parts in the earnings ratio

    # Calculate Lottie's earnings
    L = total_earnings / total_parts

    # Calculate Jerusha's earnings
    Jerusha = earnings_ratio * L

    result = Jerusha
    return result

print(solution())