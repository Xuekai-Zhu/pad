def solution():
    """Melly's two cats each have litters of kittens at the same time. The first cat has 3 blue-eyed kittens and 7 brown-eyed kittens. The second cat has 4 blue-eyed kittens and 6 brown-eyed kittens. What percentage of all the kittens have blue eyes?"""
    # Calculate the total number of kittens
    total_kittens = 3 + 7 + 4 + 6

    # Calculate the number of kittens with blue eyes
    blue_eyed_kittens = 3 + 4

    # Calculate the percentage of kittens with blue eyes
    blue_eyed_percentage = (blue_eyed_kittens / total_kittens) * 100

    # Return the result
    result = blue_eyed_percentage
    return result

print(solution())