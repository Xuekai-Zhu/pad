def solution():
    """Kameron has 100 kangaroos on his large farm; Bert has 20 kangaroos on his farm. In how many more days will Bert have the same number of kangaroos as Kameron does now if he buys kangaroos at the same rate of 2 new kangaroos per day?"""
    kam_kangaroos = 100
    bert_kangaroos = 20
    kangaroo_rate = 2
    days_needed = (kam_kangaroos - bert_kangaroos) / kangaroo_rate
    result = days_needed
    return result

print(solution())