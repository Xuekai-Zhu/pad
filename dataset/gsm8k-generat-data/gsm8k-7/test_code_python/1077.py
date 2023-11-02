def solution():
    percent_correct = 80
    num_mistakes = 5

    # Calculate the percent incorrect
    percent_incorrect = 100 - percent_correct

    # Calculate the percent incorrect as a decimal
    decimal_incorrect = percent_incorrect / 100

    # Calculate the total number of items on the quiz
    total_items = num_mistakes / decimal_incorrect
    result = total_items
    return result

print(solution())