def solution():
    """On Tuesday, a fruit vendor sold 2.5 dozen lemons and 5 dozens avocados. What is the total number of fruits that the fruit vendor sold?"""
    lemon_dozen = 2.5
    avocado_dozen = 5
    lemon_count = lemon_dozen * 12
    avocado_count = avocado_dozen * 12
    total_fruits = lemon_count + avocado_count
    result = total_fruits
    return result

print(solution())