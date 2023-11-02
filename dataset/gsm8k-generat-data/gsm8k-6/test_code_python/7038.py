def solution():
    # Calculate the number of pets remaining at the store
    remaining_puppies = 7 - 2  # two puppies sold
    remaining_kittens = 6 - 3  # three kittens sold
    total_remaining_pets = remaining_puppies + remaining_kittens
    result = total_remaining_pets
    return result

print(solution())