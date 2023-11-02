def solution():
    """Lisa has 18 more dresses than Ana. If the number of their dresses combined is 48, how many dresses does Ana have?"""
    combined_dresses = 48
    lisa_dresses = (combined_dresses + 18) / 2
    ana_dresses = combined_dresses - lisa_dresses
    result = ana_dresses
    return result

print(solution())