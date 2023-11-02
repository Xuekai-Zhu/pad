def solution():
    """It cost 50 dollars to get cats ready for adoption, 100 dollars to get adult dogs ready for adoption, and 150 to get puppies ready for adoption. If 2 cats, 3 adult dogs, and 2 puppies are adopted what was the cost to get them ready?"""
    cat_cost = 50
    dog_cost = 100
    puppy_cost = 150
    num_cats = 2
    num_dogs = 3
    num_puppies = 2
    total_cost = (cat_cost * num_cats) + (dog_cost * num_dogs) + (puppy_cost * num_puppies)
    result = total_cost
    return result

print(solution())