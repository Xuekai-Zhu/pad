def solution():
    anthony_cats = (2/3) * 12  # calculate number of cats Anthony has
    anthony_dogs = 12 - anthony_cats  # calculate number of dogs Anthony has
    leonel_cats = (1/2) * anthony_cats  # calculate number of cats Leonel has
    leonel_dogs = anthony_dogs + 7  # calculate number of dogs Leonel has
    total_animals = anthony_cats + anthony_dogs + leonel_cats + leonel_dogs  # calculate total number of animals
    result = total_animals
    return result

print(solution())