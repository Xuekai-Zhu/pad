def solution():
    """Ali had a collection of seashells. He started with 180 seashells. He then gave away 40 seashells to his friends. He also gave 30 seashells to his brothers. If he sold half of the remaining seashells, how many seashells did he have left?"""
    starting_seashells = 180
    given_to_friends = 40
    given_to_brothers = 30
    remaining_seashells = starting_seashells - given_to_friends - given_to_brothers
    sold_seashells = remaining_seashells / 2
    seashells_left = remaining_seashells - sold_seashells
    result = seashells_left
    return result

print(solution())