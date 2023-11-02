def solution():
    """Mr. Sean has a veterinary clinic where he charges clients $60 to treat a dog and $40 to care for a cat. If Khalil took 20 dogs and 60 cats to the clinic for treatment, how much money did he pay Mr. Sean?"""
    # Define the cost to treat a dog and care for a cat
    DOG_COST = 60
    CAT_COST = 40

    # Define the number of dogs and cats taken to the clinic
    num_dogs = 20
    num_cats = 60

    # Calculate the total cost for treating the dogs
    dog_total = DOG_COST * num_dogs

    # Calculate the total cost for caring for the cats
    cat_total = CAT_COST * num_cats

    # Calculate the total cost for treatment of all the animals
    total_cost = dog_total + cat_total

    # Display the total cost
    result = total_cost
    return result

print(solution())