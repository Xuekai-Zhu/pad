def solution():
    num_puppies = 2
    num_kittens = 2
    num_parakeets = 3

    parakeet_price = 10
    kitten_price = 2 * parakeet_price
    puppy_price = 3 * parakeet_price

    # Calculate the total cost of all parakeets
    total_parakeet_cost = num_parakeets * parakeet_price

    # Calculate the total cost of all kittens
    total_kitten_cost = num_kittens * kitten_price

    # Calculate the total cost of all puppies
    total_puppy_cost = num_puppies * puppy_price

    # Calculate the total cost of all pets for sale
    total_cost = total_parakeet_cost + total_kitten_cost + total_puppy_cost
    result = total_cost
    return result

print(solution())