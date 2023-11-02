def solution():
    """It cost 50 dollars to get cats ready for adoption, 100 dollars to get adult dogs ready for adoption, and 150 to get puppies ready for adoption. If 2 cats, 3 adult dogs, and 2 puppies are adopted what was the cost to get them ready?"""
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