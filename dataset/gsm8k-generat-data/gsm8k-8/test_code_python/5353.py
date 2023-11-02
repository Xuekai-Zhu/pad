def solution():
    # Define the number of puppies
    puppies = 2

    # Define the cost of each puppy and kitten
    puppy_cost = 20
    kitten_cost = 15

    # Define the total value of the stock
    total_value = 100

    # Calculate the value of the kittens
    kitten_value = total_value - (puppies * puppy_cost)

    # Calculate the number of kittens
    num_kittens = kitten_value / kitten_cost
    result = num_kittens
    return result

print(solution())