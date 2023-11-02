def solution():
    # Calculate base sentence length
    goods_stolen = 40000
    base_sentence_years = goods_stolen / 5000

    # Calculate increased sentence length for third offense
    third_offense_increase = 0.25 * base_sentence_years
    increased_sentence_years = base_sentence_years + third_offense_increase

    # Add additional 2 years for resisting arrest
    total_sentence_years = increased_sentence_years + 2
    result = total_sentence_years
    return result

print(solution())