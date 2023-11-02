def solution():
    ali_closet_capacity = 200  # Ali's closet can fit 200 pairs of jeans
    noah_closet_capacity = ali_closet_capacity / 4  # Each of Noah's closets can fit 1/4 as much as Ali's closet
    total_noah_capacity = noah_closet_capacity * 2  # Noah has two closets with the same capacity

    # Calculate the total number of jeans that Noah's closets can fit
    total_jeans_capacity = total_noah_capacity * ali_closet_capacity
    result = total_jeans_capacity
    return result

print(solution())