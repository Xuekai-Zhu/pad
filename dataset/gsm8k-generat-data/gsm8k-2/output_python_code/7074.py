def solution():
    """The owner of a small store divided the sugar into 12 packs. If each pack weighs 250 grams and has 20 grams of sugar left, how many grams of sugar did he start with?"""
    pack_weight = 250
    leftover_sugar = 20
    total_weight = pack_weight * 12
    starting_weight = total_weight + leftover_sugar
    result = starting_weight
    return result

print(solution())