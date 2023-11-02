def solution():
    """Janet has a business selling custom collars for dogs and cats. If it takes 18 inches of nylon to make a dog collar and 10 inches to make a cat collar, how much nylon does she need to make 9 dog collars and 3 cat collars?"""
    dog_collar_nylon = 18
    cat_collar_nylon = 10
    total_dog_nylon = 9 * dog_collar_nylon
    total_cat_nylon = 3 * cat_collar_nylon
    total_nylon = total_dog_nylon + total_cat_nylon
    result = total_nylon
    return result

print(solution())