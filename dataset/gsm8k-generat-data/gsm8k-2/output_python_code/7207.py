def solution():
    """Nalani had two female dogs that were expecting and after a month gave birth to 10 puppies each. She then sold 3/4 of the puppies after they came of age, each at $200. Calculate the total amount of money she received from the sale of the puppies."""
    female_dogs = 2
    puppies_per_dog = 10
    total_puppies = female_dogs * puppies_per_dog
    sold_puppies = total_puppies * 3/4
    sale_price = 200
    total_sale_amount = sold_puppies * sale_price
    result = total_sale_amount
    return result

print(solution())