def solution():
    """An apple tree produces 40 apples in its first year. The second year the apple tree produces 8 more than double the amount of apples that it produced the first year, and the third year production went down by a fourth due to an insect infestation. How many apples did the tree produce in total in the first three years?"""
    year_one_production = 40
    year_two_production = 8 + 2 * year_one_production
    year_three_production = 0.75 * year_two_production
    total_production = year_one_production + year_two_production + year_three_production
    result = total_production
    return result

print(solution())