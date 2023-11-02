def solution():
    base_sentence = 8000
    percent_increase = 25
    increase_amount = base_sentence * (percent_increase / 100)
    total_sentence = base_sentence + increase_amount + 2
    result = total_sentence
    return result

print(solution())