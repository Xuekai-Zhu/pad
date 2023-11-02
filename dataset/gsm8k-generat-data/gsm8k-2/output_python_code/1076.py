def solution():
    """Louie obtained 80% on a math quiz. He had 5 mistakes. How many items were there on the math quiz?"""
    percentage_correct = 0.8
    total_mistakes = 5
    total_items = (total_mistakes / (1 - percentage_correct)) * 100
    result = total_items
    return result

print(solution())