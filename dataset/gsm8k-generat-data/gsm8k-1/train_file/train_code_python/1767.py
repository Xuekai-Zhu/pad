def solution():
    """Jeff has a shelter where he currently takes care of 20 cats. On Monday he found 2 kittens in a box and took them to the shelter. On Tuesday he found 1 more cat with a leg injury. On Wednesday 3 people adopted 2 cats each. How many cats does Jeff currently have in his shelter?"""
    initial_cats = 20
    new_cats = 2
    injured_cats = 1
    adopted_cats = 3 * 2
    total_cats = initial_cats + new_cats + injured_cats - adopted_cats
    result = total_cats
    return result

print(solution())