def solution():
    """When Betty makes cheesecake, she sweetens it with a ratio of one part sugar to four parts cream cheese, and she flavors it with one teaspoon of vanilla for every two cups of cream cheese. For every one teaspoon of vanilla, she uses two eggs. She used two cups of sugar in her latest cheesecake. How many eggs did she use?"""
    sugar_ratio = 1
    cream_cheese_ratio = 4
    vanilla_ratio = 0.5
    egg_ratio = 2
    sugar_used = 2
    cream_cheese_used = sugar_used * cream_cheese_ratio / sugar_ratio
    vanilla_used = cream_cheese_used * vanilla_ratio
    egg_used = vanilla_used * egg_ratio
    result = egg_used
    return result

print(solution())