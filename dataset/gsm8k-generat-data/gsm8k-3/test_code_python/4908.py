def solution():
    """Noah has two closets. Each closet can fit 1/4 as much as Ali's closet, which can fit 200 pairs of jeans.  How many jeans can both Noah’s closets fit?"""
    # Define the capacity of Ali's closet
    ALI_CAPACITY = 200

    # Calculate the capacity of each of Noah's closets
    noah_capacity = ALI_CAPACITY * 1/4 * 1/2  # 1/4 because each of Noah's closets is 1/4 the size of Ali's closet, and 1/2 because Noah has two closets

    # Calculate the total capacity of both of Noah's closets
    total_capacity = noah_capacity * 2  # multiplication by 2 because Noah has two closets

    # Display the number of jeans that both of Noah's closets can fit
    result = total_capacity
    return result

print(solution())