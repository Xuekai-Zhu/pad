def solution():
    employees = 5
    Rudy_words_per_minute = 64
    Joyce_words_per_minute = 76
    Gladys_words_per_minute = 91
    Lisa_words_per_minute = 80
    Mike_words_per_minute = 89
    total_words_per_minute = Rudy_words_per_minute + Joyce_words_per_minute + Gladys_words_per_minute + Lisa_words_per_minute + Mike_words_per_minute
    average_words_per_minute = total_words_per_minute / employees
    result = average_words_per_minute
    return result

print(solution())