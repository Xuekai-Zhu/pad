def solution():
    # Calculate the return on investment for Emma and Briana after 2 years
    emma_roi = (300 * 0.15) * 2  # Emma's investment of $300 yielding 15% annually for 2 years
    briana_roi = (500 * 0.1) * 2  # Briana's investment of $500 yielding 10% annually for 2 years

    # Calculate the difference between their return on investment
    roi_difference = emma_roi - briana_roi
    result = roi_difference
    return result

print(solution())