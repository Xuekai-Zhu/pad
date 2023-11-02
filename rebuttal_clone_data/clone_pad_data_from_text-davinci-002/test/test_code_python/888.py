def solution():
    gold_stickers = 50
    silver_stickers = 2 * gold_stickers
    bronze_stickers = silver_stickers - 20
    total_stickers = gold_stickers + silver_stickers + bronze_stickers
    stickers_per_student = total_stickers / 5
    result = stickers_per_student
    return result

print(solution())