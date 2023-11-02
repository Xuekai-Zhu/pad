def solution():
    """It cost 50 dollars to get cats ready for adoption, 100 dollars to get adult dogs ready for adoption, and 150 to get puppies ready for adoption.  If 2 cats, 3 adult dogs, and 2 puppies are adopted what was the cost to get them ready?"""
    # Define the cost to get each type of animal ready for adoption
    CAT_COST = 50
    ADULT_DOG_COST = 100
    PUPPY_COST = 150

    # Define the number of each type of animal adopted
    num_cats = 2
    num_adult_dogs = 3
    num_puppies = 2

    # Calculate the total cost to get the animals ready for adoption
    total_cost = num_cats * CAT_COST + num_adult_dogs * ADULT_DOG_COST + num_puppies * PUPPY_COST

    # Display the total cost
    result = total_cost
    return result

print(solution())