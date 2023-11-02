def solution():
    """Louie obtained 80% on a math quiz. He had 5 mistakes. How many items were there on the math quiz?"""
    # Define the percentage score and number of mistakes made
    score = 80
    mistakes = 5

    # Calculate the total number of items on the quiz using the formula: 
    # total_items = (correct_items / total_items) * 100
    total_items = (score / (100 - score)) * (100 - mistakes)

    # Round up to the nearest whole number
    total_items = round(total_items)

    # return the result
    result = total_items
    return result

print(solution())