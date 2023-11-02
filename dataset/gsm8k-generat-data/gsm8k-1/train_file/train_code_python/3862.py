def solution():
    """It takes 2.5 hours to groom a dog and 0.5 hours to groom a cat. What is the number of minutes it takes to groom 5 dogs and 3 cats?"""
    dog_time = 2.5 * 60 # converting hours to minutes
    cat_time = 0.5 * 60 # converting hours to minutes
    num_dogs = 5
    num_cats = 3
    total_time = (dog_time * num_dogs) + (cat_time * num_cats)
    result = total_time
    return result

print(solution())