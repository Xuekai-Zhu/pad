def solution():
    """Ali had a collection of seashells. He started with 180 seashells. He then gave away 40 seashells to his friends. He also gave 30 seashells to his brothers. If he sold half of the remaining seashells, how many seashells did he have left?"""
    starting_count = 180
    friends_count = 40
    brothers_count = 30
    remaining_count = starting_count - friends_count - brothers_count
    sold_count = remaining_count / 2
    final_count = remaining_count - sold_count
    result = final_count
    return result

print(solution())