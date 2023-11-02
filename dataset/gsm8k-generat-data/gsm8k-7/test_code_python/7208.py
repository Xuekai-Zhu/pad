def solution():
    num_female_dogs = 2
    puppies_per_dog = 10
    total_puppies = num_female_dogs * puppies_per_dog
    sold_fraction = 3/4
    sale_price = 200

    # Calculate the total number of puppies sold
    num_sold = total_puppies * sold_fraction

    # Calculate the total amount received from the sale of puppies
    total_sale_amount = num_sold * sale_price
    result = total_sale_amount
    return result

print(solution())