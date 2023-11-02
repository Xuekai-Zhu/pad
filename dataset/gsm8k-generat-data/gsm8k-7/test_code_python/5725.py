def solution():
    words_per_day = 10
    days_per_year = 365
    years = 2

    # Calculate the number of words Tim learns in 2 years
    words_learned = words_per_day * days_per_year * years

    # Calculate the original number of words Tim knew before the book
    original_knowledge = words_learned / 1.5

    result = original_knowledge
    return result

print(solution())