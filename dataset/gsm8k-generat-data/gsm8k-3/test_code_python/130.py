def solution():
    """Ali had a collection of seashells. He started with 180 seashells. He then gave away 40 seashells to his friends. He also gave 30 seashells to his brothers. If he sold half of the remaining seashells, how many seashells did he have left?"""
    # Define the initial number of seashells
    initial_seashells = 180

    # Calculate the number of seashells given away
    given_seashells = 40 + 30

    # Calculate the number of seashells remaining
    remaining_seashells = initial_seashells - given_seashells

    # Calculate the number of seashells sold
    sold_seashells = remaining_seashells / 2

    # Calculate the number of seashells remaining
    remaining_seashells -= sold_seashells

    result = remaining_seashells
    return result

print(solution())