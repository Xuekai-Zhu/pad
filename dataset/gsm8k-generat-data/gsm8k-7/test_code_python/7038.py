def solution():
    num_puppies = 7
    num_kittens = 6

    # Calculate the number of puppies and kittens sold
    num_puppies_sold = 2
    num_kittens_sold = 3

    # Calculate the remaining number of puppies and kittens
    num_puppies_remaining = num_puppies - num_puppies_sold
    num_kittens_remaining = num_kittens - num_kittens_sold

    # Calculate the total number of pets remaining
    total_pets_remaining = num_puppies_remaining + num_kittens_remaining
    result = total_pets_remaining
    return result

print(solution())