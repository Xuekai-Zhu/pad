def solution():
    # Calculate the remaining number of animals in the pet store
    remaining_birds = 12 // 2   # half the birds were sold, so remaining birds are the integer quotient of 12 divided by 2
    remaining_puppies = 9 - 3   # 3 puppies were adopted, so remaining puppies are the difference between 9 and 3
    remaining_cats = 5         # all cats remain
    remaining_spiders = 15 - 7  # 7 spiders went loose, so remaining spiders are the difference between 15 and 7
    total_remaining_animals = remaining_birds + remaining_puppies + remaining_cats + remaining_spiders
    result = total_remaining_animals
    return result

print(solution())