def solution():
    """Miss Walter has 50 gold stickers. She also has twice as many silver stickers as gold stickers, and 20 fewer bronze stickers than silver stickers. She wants to give the same number of stickers to each of her 5 students. How many stickers will each student receive?"""
    gold_stickers = 50
    silver_stickers = gold_stickers * 2
    bronze_stickers = silver_stickers - 20
    total_stickers = gold_stickers + silver_stickers + bronze_stickers
    stickers_per_student = total_stickers / 5
    result = stickers_per_student
    return result

print(solution())