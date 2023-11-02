def solution():
    puppy_cost = 20  # Cost of a puppy
    kitten_cost = 15  # Cost of a kitten
    total_stock_value = 100  # Total stock value is $100
    num_puppies = 2  # The pet shop has 2 puppies
    puppy_value = num_puppies * puppy_cost  # Value of puppies in stock

    # Calculate the value of the kittens in stock
    kitten_value = total_stock_value - puppy_value
    num_kittens = kitten_value / kitten_cost  # Calculate the number of kittens in stock
    result = num_kittens
    return result

print(solution())