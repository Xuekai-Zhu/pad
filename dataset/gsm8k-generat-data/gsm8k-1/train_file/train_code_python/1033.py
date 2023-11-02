def solution():
    """When Betty makes cheesecake, she sweetens it with a ratio of one part sugar to four parts cream cheese,
    and she flavors it with one teaspoon of vanilla for every two cups of cream cheese.
    For every one teaspoon of vanilla, she uses two eggs. She used two cups of sugar in her latest cheesecake. 
    How many eggs did she use?"""
    
    sugar = 2  # cups of sugar
    cream_cheese = sugar * 4  # ratio of 1 part sugar to 4 parts cream cheese
    vanilla = cream_cheese // 2  # 1 teaspoon of vanilla for every 2 cups of cream cheese
    eggs = vanilla * 2  # 2 eggs for every 1 teaspoon of vanilla
    result = eggs
    
    return result

print(solution())