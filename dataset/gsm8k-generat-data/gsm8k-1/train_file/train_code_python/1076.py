def solution():
    """Louie obtained 80% on a math quiz. He had 5 mistakes. How many items were there on the math quiz?"""
    percent_correct = 80
    mistakes = 5
    total_items = (100 - percent_correct) / percent_correct * mistakes
    total_items += mistakes
    result = total_items
    return result

print(solution())