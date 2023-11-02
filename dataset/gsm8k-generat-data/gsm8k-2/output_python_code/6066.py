def solution():
    """Michael has 36 pets. 25% of them are dogs, 50% are cats, and the rest are bunnies. How many bunnies does he have?"""
    total_pets = 36
    dog_percent = 0.25
    cat_percent = 0.5
    dog_count = total_pets * dog_percent
    cat_count = total_pets * cat_percent
    bunny_count = total_pets - dog_count - cat_count
    result = bunny_count
    return result

print(solution())