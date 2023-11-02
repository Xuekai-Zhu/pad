def solution():
    """Vann is a veterinarian. Today he is going to be doing dental cleanings only. Dogs have 42 teeth, cats have 30 teeth and pigs have 28 teeth. If he is to do 5 dogs, 10 cats and 7 pigs, how many total teeth will Vann clean today?"""
    dog_teeth = 42
    cat_teeth = 30
    pig_teeth = 28
    num_dogs = 5
    num_cats = 10
    num_pigs = 7
    total_teeth = dog_teeth*num_dogs + cat_teeth*num_cats + pig_teeth*num_pigs
    result = total_teeth
    return result

print(solution())