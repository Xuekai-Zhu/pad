def solution():
    puppies_for_sale = 7
    kittens_for_sale = 6
    puppies_sold = 2
    kittens_sold = 3

    remaining_puppies = puppies_for_sale - puppies_sold
    remaining_kittens = kittens_for_sale - kittens_sold

    total_remaining_pets = remaining_puppies + remaining_kittens
    result = total_remaining_pets
    return result

print(solution())