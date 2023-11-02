def solution():
    """An apple tree produces 40 apples in its first year. The second year the apple tree produces 8 more than double the amount of apples that it produced the first year, and the third year production went down by a fourth due to an insect infestation. How many apples did the tree produce in total in the first three years?"""
    first_year_apples = 40
    second_year_apples = 8 + 2 * first_year_apples
    third_year_apples = int(3 / 4 * second_year_apples)
    total_apples = first_year_apples + second_year_apples + third_year_apples
    result = total_apples
    return result

print(solution())