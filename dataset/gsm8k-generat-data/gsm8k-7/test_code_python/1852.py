def solution():
    kam_kangaroos = 100
    bert_kangaroos = 20
    kangaroo_rate = 2

    # Calculate the number of days it will take for Bert to catch up to Kameron
    days_to_catch_up = (kam_kangaroos - bert_kangaroos) / kangaroo_rate
    result = days_to_catch_up
    return result

print(solution())