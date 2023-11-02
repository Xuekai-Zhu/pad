def solution():
    """At the pet store, there are 7 puppies and 6 kittens for sale. Two puppies and three kittens are sold. How many pets remain at the store?"""
    # Define the initial number of puppies and kittens
    initial_puppies = 7
    initial_kittens = 6

    # Define the number of puppies and kittens sold
    sold_puppies = 2
    sold_kittens = 3

    # Calculate the remaining number of puppies and kittens
    remaining_puppies = initial_puppies - sold_puppies
    remaining_kittens = initial_kittens - sold_kittens

    # Return the total number of remaining pets
    result = remaining_puppies + remaining_kittens
    return result

print(solution())