def solution():
    """Miss Walter has 50 gold stickers. She also has twice as many silver stickers as gold stickers, and 20 fewer bronze stickers than silver stickers.  She wants to give the same number of stickers to each of her 5 students. How many stickers will each student receive?"""
    # Define the number of gold stickers
    gold_stickers = 50

    # Calculate the number of silver stickers
    silver_stickers = gold_stickers * 2

    # Calculate the number of bronze stickers
    bronze_stickers = silver_stickers - 20

    # Calculate the total number of stickers
    total_stickers = gold_stickers + silver_stickers + bronze_stickers

    # Calculate the number of stickers each student will receive
    stickers_per_student = total_stickers // 5

    # Display the number of stickers each student will receive
    result = stickers_per_student
    return result

print(solution())