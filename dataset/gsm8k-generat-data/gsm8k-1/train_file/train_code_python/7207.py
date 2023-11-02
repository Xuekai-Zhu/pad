def solution():
    """Nalani had two female dogs that were expecting and after a month gave birth to 10 puppies each.
    She then sold 3/4 of the puppies after they came of age, each at $200. Calculate the total amount of money she received from the sale of the puppies."""
    puppies_per_dog = 10
    number_of_dogs = 2
    total_puppies = puppies_per_dog * number_of_dogs
    puppies_sold = total_puppies * (3/4)
    price_per_puppy = 200
    total_money_received = puppies_sold * price_per_puppy
    result = total_money_received
    return result

print(solution())