def solution():
    # Calculate Emma's return on investment after 2 years
    emma_roi = 300 * (1 + 0.15)**2

    # Calculate Briana's return on investment after 2 years
    briana_roi = 500 * (1 + 0.10)**2

    # Calculate the difference between their return on investment
    roi_difference = emma_roi - briana_roi
    result = roi_difference
    return result

print(solution())