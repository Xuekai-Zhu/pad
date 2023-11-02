def solution():
    """Mr. Sean has a veterinary clinic where he charges clients $60 to treat a dog and $40 to care for a cat. If Khalil took 20 dogs and 60 cats to the clinic for treatment, how much money did he pay Mr. Sean?"""
    dog_price = 60
    cat_price = 40
    num_dogs = 20
    num_cats = 60
    total_price = (num_dogs * dog_price) + (num_cats * cat_price)
    result = total_price
    return result

print(solution())