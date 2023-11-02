def solution():
    # Calculate the total number of puppies Nalani had
    total_puppies = 10 + 10  # Two dogs gave birth to 10 puppies each

    # Calculate the number of puppies she sold after they came of age
    sold_puppies = (3/4) * total_puppies

    # Calculate the total amount of money she received from selling the puppies
    total_amount = sold_puppies * 200  # Each puppy was sold for $200

    result = total_amount
    return result

print(solution())