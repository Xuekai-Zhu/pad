def solution():
    kameron_kangaroos = 100  # Kameron has 100 kangaroos
    bert_kangaroos = 20  # Bert has 20 kangaroos
    rate = 2  # Bert buys kangaroos at a rate of 2 new kangaroos per day

    days_needed = (kameron_kangaroos - bert_kangaroos) / rate  # Calculate the number of days needed to reach the same number of kangaroos
    result = days_needed
    return result

print(solution())