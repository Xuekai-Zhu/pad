def solution():
    """Jason is tired of the neighborhood animals raiding his trash. He pepper-sprays some raccoons and 6 times as many squirrels. If he pepper-sprays 84 animals total, how many raccoons does he pepper-spray?"""
    total_animals = 84
    squirrel_ratio = 6
    raccoon_and_squirrel = total_animals / (squirrel_ratio + 1)
    raccoon_count = raccoon_and_squirrel
    result = raccoon_count
    return result

print(solution())