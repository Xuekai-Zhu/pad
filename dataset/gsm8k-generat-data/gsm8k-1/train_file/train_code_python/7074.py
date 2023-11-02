def solution():
    """The owner of a small store divided the sugar into 12 packs. If each pack weighs 250 grams and has 20 grams of sugar left, how many grams of sugar did he start with?"""
    sugar_per_pack = 250
    sugar_left_over = 20
    total_sugar = (sugar_per_pack - sugar_left_over) * 12
    result = total_sugar
    return result

print(solution())