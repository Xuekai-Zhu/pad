def solution():
    # Calculate the number of items on the math quiz
    score = 0.8  # Louie's score on the math quiz is 80%
    num_mistakes = 5
    total_items = (100 / score) * (num_mistakes / 100 + 1)  # formula: total_items = (100 / score) * (num_mistakes / 100 + 1)
    result = int(total_items)  # round down to the nearest integer
    return result

print(solution())