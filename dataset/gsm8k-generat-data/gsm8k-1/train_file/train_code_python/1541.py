def solution():
    """Janet has a business selling custom collars for dogs and cats. If it takes 18 inches of nylon to make a dog collar and 10 inches to make a cat collar, how much nylon does she need to make 9 dog collars and 3 cat collars?"""
    dog_collar_inches = 18
    cat_collar_inches = 10
    num_dog_collars = 9
    num_cat_collars = 3
    total_inches = (dog_collar_inches * num_dog_collars) + (cat_collar_inches * num_cat_collars)
    result = total_inches
    return result

print(solution())