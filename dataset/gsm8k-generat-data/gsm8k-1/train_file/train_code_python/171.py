def solution():
    """Kyle bought 2 glass bottles that can hold 15 origami stars each. He then bought another 3 identical glass bottles. How many stars must Kyle make to fill all the glass bottles he bought?"""
    bottles_with_stars = 2
    star_capacity = 15
    total_stars = bottles_with_stars * star_capacity
    remaining_bottles = 3
    total_bottles = bottles_with_stars + remaining_bottles
    stars_needed = total_bottles * star_capacity
    result = stars_needed
    return result

print(solution())