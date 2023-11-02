def solution():
    """An apple tree produces 40 apples in its first year. The second year the apple tree produces 8 more than double the amount of apples that it produced the first year, and the third year production went down by a fourth due to an insect infestation. How many apples did the tree produce in total in the first three years?"""
    # Define the number of apples produced in the first year
    year1_apples = 40

    # Calculate the number of apples produced in the second year
    year2_apples = (2 * year1_apples) + 8

    # Calculate the number of apples produced in the third year
    year3_apples = year2_apples - (year2_apples // 4)

    # Calculate the total number of apples produced in the first three years
    total_apples = year1_apples + year2_apples + year3_apples

    result = total_apples
    return result

print(solution())