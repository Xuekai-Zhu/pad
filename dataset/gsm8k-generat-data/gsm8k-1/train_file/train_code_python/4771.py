def solution():
    """Vann is a veterinarian. Today he is going to be doing dental cleanings only. Dogs have 42 teeth, cats have 30 teeth and pigs have 28 teeth. If he is to do 5 dogs, 10 cats and 7 pigs, how many total teeth will Vann clean today?"""
    dogs = 5
    cats = 10
    pigs = 7
    dog_teeth = 42
    cat_teeth = 30
    pig_teeth = 28
    total_teeth = (dogs * dog_teeth) + (cats * cat_teeth) + (pigs * pig_teeth)
    result = total_teeth
    return result

print(solution())