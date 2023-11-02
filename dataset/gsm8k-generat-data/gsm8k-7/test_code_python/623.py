def solution():
    # Fraction of lemonade in one drink
    fraction_lemonade = 1.25 / (1.25 + 0.25)  # 1.25 cups of lemonade out of a total of 1.5 cups

    # Total lemonade in pitcher
    total_lemonade = fraction_lemonade * 18
    result = total_lemonade
    return result

print(solution())