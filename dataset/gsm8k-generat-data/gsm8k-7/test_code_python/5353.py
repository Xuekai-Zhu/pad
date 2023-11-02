def solution():
    num_puppies = 2
    puppy_price = 20
    kitten_price = 15
    total_stock_value = 100

    # Calculate the total value of all puppies
    total_puppy_value = num_puppies * puppy_price

    # Calculate the total value of all kittens
    total_kitten_value = total_stock_value - total_puppy_value

    # Calculate the number of kittens
    num_kittens = total_kitten_value // kitten_price
    result = num_kittens
    return result

print(solution())