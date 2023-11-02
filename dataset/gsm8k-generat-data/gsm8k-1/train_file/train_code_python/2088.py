def solution():
    """Sophia ate 1/6 of her pie and she put the rest on the fridge. If the pie left in the fridge weighs 1200 grams, how many grams did Sophia eat?"""
    pie_left = 1200
    pie_total = pie_left / (1/6)
    pie_eaten = pie_total - pie_left
    result = pie_eaten
    return result

print(solution())