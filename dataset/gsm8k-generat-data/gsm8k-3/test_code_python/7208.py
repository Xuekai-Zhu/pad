def solution():
    """Nalani had two female dogs that were expecting and after a month gave birth to 10 puppies each.
     She then sold 3/4 of the puppies after they came of age, each at $200. Calculate the total amount of money
      she received from the sale of the puppies."""

    # Calculate the total number of puppies
    total_puppies = 2 * 10

    # Calculate the number of puppies she sold
    sold_puppies = total_puppies * 3 / 4

    # Calculate the total amount of money she received from the sale
    total_money = sold_puppies * 200

    result = total_money
    return result

print(solution())