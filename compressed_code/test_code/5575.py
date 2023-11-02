def solution():
    
    female_dogs = 2
    puppies_per_dog = 10
    total_puppies = female_dogs * puppies_per_dog
    sold_puppies = total_puppies * 3/4
    sale_price = 200
    total_sale_amount = sold_puppies * sale_price
    result = total_sale_amount
    return result

print(solution())