def solution():
    """Sammy can eat 15 pickle slices. His twin sister Tammy can eat twice as much as Sammy. Their older brother Ron eats 20% fewer pickles slices than Tammy. How many pickle slices does Ron eat?"""
    sammy_pickles = 15
    tammy_pickles = 2 * sammy_pickles
    ron_pickles = tammy_pickles - (0.2 * tammy_pickles)
    result = ron_pickles
    return result

print(solution())