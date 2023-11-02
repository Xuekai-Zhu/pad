def solution():
    """Nalani had two female dogs that were expecting and after a month gave birth to 10 puppies each. She then sold 3/4 of the puppies after they came of age, each at $200. Calculate the total amount of money she received from the sale of the puppies."""
    # Define the number of female dogs Nalani had
    female_dogs = 2

    # Define the number of puppies each dog gave birth to
    puppies_per_dog = 10

    # Calculate the total number of puppies
    total_puppies = female_dogs * puppies_per_dog

    # Calculate the number of puppies sold
    sold_puppies = total_puppies * (3/4)

    # Calculate the total amount of money received from the sale
    sale_amount = sold_puppies * 200

    # return the result
    result = sale_amount
    return result

print(solution())