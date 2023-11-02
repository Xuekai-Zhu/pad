def solution():
    """At the pet store, there are 7 puppies and 6 kittens for sale. Two puppies and three kittens are sold. How many pets remain at the store?"""
    puppies = 7
    kittens = 6
    puppies_sold = 2
    kittens_sold = 3
    puppies_remaining = puppies - puppies_sold
    kittens_remaining = kittens - kittens_sold
    total_remaining = puppies_remaining + kittens_remaining
    result = total_remaining
    return result

print(solution())