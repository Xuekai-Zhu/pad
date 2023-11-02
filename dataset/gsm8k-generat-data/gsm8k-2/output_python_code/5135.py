def solution():
    """Mario has 3 hibiscus plants in his garden. The first hibiscus plant has 2 flowers. The second hibiscus plant has twice as many flowers as the first hibiscus plant. The third hibiscus plant has four times as many flowers as the second hibiscus plant. How many total blossoms does Mario have?"""
    first_hibiscus = 2
    second_hibiscus = 2 * first_hibiscus
    third_hibiscus = 4 * second_hibiscus
    total_blossoms = first_hibiscus + second_hibiscus + third_hibiscus
    result = total_blossoms
    return result

print(solution())