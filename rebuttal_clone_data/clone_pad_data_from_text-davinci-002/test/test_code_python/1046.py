def solution():
    kameron_kangaroos = 100
    bert_kangaroos = 20
    bert_kangaroos_per_day = 2
    days_until_equal = (kameron_kangaroos - bert_kangaroos) / bert_kangaroos_per_day
    result = days_until_equal
    return result

print(solution())