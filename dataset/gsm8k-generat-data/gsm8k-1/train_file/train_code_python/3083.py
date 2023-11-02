def solution():
    """Susan is picking strawberries. She's trying to fill her basket, but out of every handful of 5 strawberries she can't help but eat one of them herself. If her basket holds 60 strawberries, how many berries will she actually pick before she fills it?"""
    berries_per_handful = 5
    eaten_per_handful = 1
    picked_per_handful = berries_per_handful - eaten_per_handful
    basket_size = 60
    picked_so_far = 0
    while picked_so_far < basket_size:
        picked_so_far += picked_per_handful
    berries_picked = picked_so_far
    result = berries_picked
    return result

print(solution())