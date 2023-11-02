def solution():
    """Bob bought 2 show dogs for $250.00 each to breed as a side business. The female just had a litter of 6 puppies. If he sells each puppy for $350.00, what is his total profit?"""
    cost_per_dog = 250
    number_of_dogs = 2
    total_cost = cost_per_dog * number_of_dogs
    price_per_puppy = 350
    number_of_puppies = 6
    total_income = price_per_puppy * number_of_puppies
    total_profit = total_income - total_cost
    result = total_profit
    return result

print(solution())