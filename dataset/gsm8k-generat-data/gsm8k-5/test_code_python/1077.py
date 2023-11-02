def solution():
    percent_correct = 80  # Louie obtained 80% on the math quiz
    num_errors = 5  # Louie had 5 mistakes on the math quiz

    # Calculate the percentage of items Louie answered correctly
    percent_answered_correctly = 100 - percent_correct

    # Calculate the total number of items on the math quiz
    total_items = (100 * num_errors) / percent_answered_correctly
    result = total_items
    return result

print(solution())