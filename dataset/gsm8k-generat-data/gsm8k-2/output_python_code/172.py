def solution():
    """Kyle bought 2 glass bottles that can hold 15 origami stars each. He then bought another 3 identical glass bottles. How many stars must Kyle make to fill all the glass bottles he bought?"""
    num_bottles = 2 + 3
    stars_per_bottle = 15
    total_stars_needed = num_bottles * stars_per_bottle
    result = total_stars_needed
    return result

print(solution())