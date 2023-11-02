def solution():
    kindergarten_age_range = list(range(4,7))
    alphabet_learning_task = True
    if max(kindergarten_age_range) < 7 and alphabet_learning_task:
        result = "no"
    else:
        result = "yes"
    return result

print(solution())