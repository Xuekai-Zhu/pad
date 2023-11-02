def solution():
    """Melly's two cats each have litters of kittens at the same time. The first cat has 3 blue-eyed kittens and 7 brown-eyed kittens. The second cat has 4 blue-eyed kittens and 6 brown-eyed kittens. What percentage of all the kittens have blue eyes?"""
    total_blue_eyes = 3 + 4
    total_kittens = 3 + 7 + 4 + 6
    percentage_blue_eyes = (total_blue_eyes / total_kittens) * 100
    result = percentage_blue_eyes
    return result

print(solution())