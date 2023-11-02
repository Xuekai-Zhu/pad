def solution():
    # Calculate the number of dogs Carly worked on
    dogs_with_four_paws = 164 // 4  # Each dog has 4 paws with nails, so divide by 4 to get the number of dogs
    dogs_with_three_paws = 3  # Carly mentions that 3 dogs had only 3 legs
    total_dogs = dogs_with_four_paws + dogs_with_three_paws
    result = total_dogs
    return result

print(solution())