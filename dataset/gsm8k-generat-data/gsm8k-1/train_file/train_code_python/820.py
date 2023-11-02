def solution():
    """Sammy can eat 15 pickle slices. His twin sister Tammy can eat twice as much as Sammy. Their older brother Ron eats 20% fewer pickles slices than Tammy. How many pickle slices does Ron eat?"""
    sammy_slices = 15
    tammy_slices = sammy_slices * 2
    ron_slices = tammy_slices - (tammy_slices * 0.20)
    result = ron_slices
    return result

print(solution())