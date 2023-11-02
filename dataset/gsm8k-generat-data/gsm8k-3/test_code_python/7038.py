def solution():
    """At the pet store, there are 7 puppies and 6 kittens for sale. Two puppies and three kittens are sold. How many pets remain at the store?"""
    # Define the initial number of puppies and kittens
    initial_puppies = 7
    initial_kittens = 6

    # Define the number of puppies and kittens sold
    puppies_sold = 2
    kittens_sold = 3

    # Calculate the remaining number of puppies and kittens
    remaining_puppies = initial_puppies - puppies_sold
    remaining_kittens = initial_kittens - kittens_sold

    # Calculate the total number of pets remaining at the store
    total_pets_remaining = remaining_puppies + remaining_kittens

    # Display the total number of pets remaining at the store
    result = total_pets_remaining
    return result

print(solution())