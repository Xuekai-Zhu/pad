def solution():
    """It cost 50 dollars to get cats ready for adoption, 100 dollars to get adult dogs ready for adoption, and 150 to get puppies ready for adoption. If 2 cats, 3 adult dogs, and 2 puppies are adopted what was the cost to get them ready?"""
    # Define the cost of getting each animal ready for adoption
    CAT_COST = 50
    DOG_COST = 100
    PUPPY_COST = 150

    # Define the number of each animal that was adopted
    num_cats = 2
    num_dogs = 3
    num_puppies = 2

    # Calculate the total cost of getting the adopted animals ready for adoption
    total_cost = (num_cats * CAT_COST) + (num_dogs * DOG_COST) + (num_puppies * PUPPY_COST)

    # return the result
    result = total_cost
    return result

print(solution())