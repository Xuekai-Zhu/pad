def solution():
    total_judges = 40
    under_30 = 0.1 * total_judges
    thirty_to_fifty = 0.6 * total_judges

    over_fifty = total_judges - under_30 - thirty_to_fifty
    result = over_fifty
    return result

print(solution())