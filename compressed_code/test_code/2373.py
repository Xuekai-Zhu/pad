def solution():
    
    cat_cost = 50
    adult_dog_cost = 100
    puppy_cost = 150
    adopted_cats = 2
    adopted_adult_dogs = 3
    adopted_puppies = 2
    total_cost = (adopted_cats * cat_cost) + (adopted_adult_dogs * adult_dog_cost) + (adopted_puppies * puppy_cost)
    result = total_cost
    return result

print(solution())