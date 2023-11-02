def solution():
    """Elois needs 4 bananas to make 1 loaf of banana bread.  On Monday, she makes 3 loaves of banana bread.  On Tuesday, she makes twice as many loaves of banana bread as Monday.  How many bananas did she use to make all the banana bread?"""
    # Define the number of bananas per loaf of banana bread
    BANANAS_PER_LOAF = 4

    # Calculate the number of loaves of banana bread made on Monday
    loaves_monday = 3

    # Calculate the number of loaves of banana bread made on Tuesday
    loaves_tuesday = loaves_monday * 2

    # Calculate the total number of loaves of banana bread made
    total_loaves = loaves_monday + loaves_tuesday

    # Calculate the total number of bananas used to make all the banana bread
    total_bananas = total_loaves * BANANAS_PER_LOAF

    # Display the total number of bananas used
    result = total_bananas
    return result

print(solution())