def solution():
    total_items = 100

    lowella_percent = 0.35
    lowella_correct = total_items * lowella_percent

    pamela_percent = lowella_percent * 1.2
    pamela_correct = total_items * pamela_percent

    mandy_correct = pamela_correct * 2

    result = mandy_correct
    return result

print(solution())