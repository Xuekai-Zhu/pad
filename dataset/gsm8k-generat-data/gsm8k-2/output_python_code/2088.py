def solution():
    """Sophia ate 1/6 of her pie and she put the rest on the fridge. If the pie left in the fridge weighs 1200 grams, how many grams did Sophia eat?"""
    pie_left = 1200
    fraction_eaten = 1/6
    total_pie = pie_left / fraction_eaten
    eaten_pie = total_pie - pie_left
    result = eaten_pie
    return result

print(solution())