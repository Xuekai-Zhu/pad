def solution():
    initial_number = 1
    number_after_four_days = 810
    number_doubled = number_after_four_days / initial_number
    number_tripled = number_doubled / initial_number
    number_of_bedbugs = number_tripled ** (1/4)
    result = number_of_bedbugs
    return result

print(solution())