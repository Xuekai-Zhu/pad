def solution():
    dog_cost = 60  # Mr. Sean charges $60 to treat a dog
    cat_cost = 40  # Mr. Sean charges $40 to care for a cat
    num_dogs = 20  # Khalil took 20 dogs to the clinic
    num_cats = 60  # Khalil took 60 cats to the clinic

    # Calculate the total cost for treating all the dogs and caring for all the cats
    total_cost = (dog_cost * num_dogs) + (cat_cost * num_cats)
    result = total_cost
    return result

print(solution())