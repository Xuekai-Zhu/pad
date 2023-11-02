def solution():
    # Calculate the total number of cookies baked by Zach on Monday and Tuesday
    total_cooked_on_Monday_and_Tuesday = 32 + (32/2)  # On Tuesday he baked half the number of cookies he baked the day before

    # Calculate the total number of cookies baked by Zach on Wednesday
    total_cooked_on_Wednesday = 3 * (32/2) - 4  # Three times the number of cookies he did on Tuesday, but his brother ate 4 of those cookies

    # Calculate the total number of cookies Zach had at the end of the three days
    total_cooked = total_cooked_on_Monday_and_Tuesday + total_cooked_on_Wednesday

    result = total_cooked
    return result

print(solution())