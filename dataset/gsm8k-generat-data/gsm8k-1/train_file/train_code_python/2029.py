def solution():
    """On Tuesday, a fruit vendor sold 2.5 dozen lemons and 5 dozens avocados. What is the total number of fruits that the fruit vendor sold?"""
    lemons_dozen = 2.5
    avocados_dozen = 5
    lemons_sold = lemons_dozen * 12
    avocados_sold = avocados_dozen * 12
    total_fruits_sold = lemons_sold + avocados_sold
    result = total_fruits_sold
    return result

print(solution())