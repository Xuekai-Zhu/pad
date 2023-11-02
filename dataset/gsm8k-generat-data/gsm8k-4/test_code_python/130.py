def solution():
    """Ali had a collection of seashells. He started with 180 seashells. He then gave away 40 seashells to his friends. He also gave 30 seashells to his brothers. If he sold half of the remaining seashells, how many seashells did he have left?"""
    # Define the initial number of seashells
    initial_seashells = 180

    # Subtract the seashells given to friends and brothers
    remaining_seashells = initial_seashells - 40 - 30

    # Sell half of the remaining seashells
    sold_seashells = remaining_seashells / 2

    # Calculate the final number of seashells
    final_seashells = remaining_seashells - sold_seashells

    result = final_seashells
    return result

print(solution())