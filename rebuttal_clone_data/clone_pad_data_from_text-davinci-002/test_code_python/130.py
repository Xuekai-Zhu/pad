def solution():
    """Ali had a collection of seashells. He started with 180 seashells. He then gave away 40 seashells to his friends. He also gave 30 seashells to his brothers. If he sold half of the remaining seashells, how many seashells did he have left?"""
    seashells_collected = 180
    seashells_given_away = 40 + 30
    seashells_left = seashells_collected - seashells_given_away
    seashells_sold = seashells_left / 2
    seashells_remaining = seashells_left - seashells_sold
    result = seashells_remaining
    return result

print(solution())