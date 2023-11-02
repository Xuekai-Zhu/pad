def solution():
    """An apple tree produces 40 apples in its first year.  The second year the apple tree produces 8 more than double the amount of apples that it produced the first year, and the third year production went down by a fourth due to an insect infestation.  How many apples did the tree produce in total in the first three years?"""
    # Define the number of apples produced in the first year
    apples_1 = 40

    # Calculate the number of apples produced in the second year
    apples_2 = 8 + 2 * apples_1

    # Calculate the number of apples produced in the third year
    apples_3 = 0.75 * apples_2

    # Calculate the total number of apples produced in the first three years
    total_apples = apples_1 + apples_2 + apples_3

    # Display the total number of apples produced
    result = total_apples
    return result

print(solution())