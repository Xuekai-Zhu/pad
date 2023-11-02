def solution():
    """Grandpa loves to eat jelly beans, but how many jelly beans he can eat depends on the size of the beans. It takes 75 large jelly beans to fill Grandpa up. He can eat twice as many medium-sized beans as large beans. And eating 3 small beans is the same as eating 1 medium-sized bean. How many small beans can Grandpa eat?"""
    large_beans = 75
    medium_beans = large_beans * 2
    small_beans = medium_beans * 3
    result = small_beans
    return result

print(solution())