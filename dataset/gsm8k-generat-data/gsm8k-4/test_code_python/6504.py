def solution():
    """Bob bought 2 show dogs for $250.00 each to breed as a side business. The female just had a litter of 6 puppies. If he sells each puppy for $350.00, what is his total profit?"""
    # Define the price of each dog and the number of dogs
    dog_price = 250
    num_dogs = 2

    # Calculate the cost of purchasing the dogs
    total_cost = dog_price * num_dogs

    # Calculate the earnings from selling the puppies
    puppy_price = 350
    num_puppies = 6
    total_earnings = puppy_price * num_puppies

    # Calculate the total profit
    total_profit = total_earnings - total_cost

    # Return the result
    result = total_profit
    return result

print(solution())