def solution():
    """Mr. Sean has a veterinary clinic where he charges clients $60 to treat a dog and $40 to care for a cat. If Khalil took 20 dogs and 60 cats to the clinic for treatment, how much money did he pay Mr. Sean?"""
    dog_treatment_cost = 60
    cat_treatment_cost = 40
    num_dogs = 20
    num_cats = 60
    total_cost = (dog_treatment_cost * num_dogs) + (cat_treatment_cost * num_cats)
    result = total_cost
    return result

print(solution())