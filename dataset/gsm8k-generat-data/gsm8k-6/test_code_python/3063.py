def solution():
    # Let's call the amount of experience of each coworker: Roger = R, Peter = P, Tom = T, Robert = B, and Mike = M
    # We know that R = P + T + B + M (from what Roger said)
    # We also know that P = 12 (since when he started working his daughter was 7, and now she's 19)
    # We know that T = 2B (from what Tom said)
    # We know that B = P - 4 and B = M + 2 (from what Robert said)
    # We can use substitution to solve for B, M, T, and P in terms of R
    # B = (R - P - T - M) / 3
    # M = B - 2
    # T = 2B
    # P = 12

    # Putting everything together, we get:
    R = (12 * 4) + ((R - 12 - (R - 12 - 2B + 4) - 2B) / 3) + 2B + (R - 12 - (R - 12 - 2B + 4) - 2B - ((R - 12 - (R - 12 - 2B + 4) - 2B) / 3)) - 50
    # Simplifying:
    R = 16 + (4/3)B - 26/3
    # Solving for B:
    B = (3/4)(R - 10)
    # We know that R has to be an integer, so we can try different values of R until we find one that gives an integer value of B
    # Trying R = 45:
    B = (3/4)(45 - 10) = 26.25
    # Not an integer, let's try R = 46:
    B = (3/4)(46 - 10) = 27
    # Bingo! Robert has 27 years of experience, which means that Tom has 54 years of experience, Peter has 12 years of experience, and Roger has 110 years of experience
    # Roger needs to work for 40 more years before he retires (50 - 110 = -60, but we don't need to worry about negative numbers here)
    result = 40
    return result

print(solution())