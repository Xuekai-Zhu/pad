def solution():
    num_dogs = 5
    dog_teeth = 42

    num_cats = 10
    cat_teeth = 30

    num_pigs = 7
    pig_teeth = 28

    # Calculate the total number of teeth Vann will clean
    total_teeth_cleaned = (num_dogs * dog_teeth) + (num_cats * cat_teeth) + (num_pigs * pig_teeth)
    result = total_teeth_cleaned
    return result

print(solution())