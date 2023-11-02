def solution():
    cats_now = 20  # Given that there are 20 cats now
    dogs_now = 2 * cats_now  # Given that there are twice as many dogs as cats now
    dogs_originally = dogs_now - 20  # Given that 20 new dogs were born
    cats_originally = 2 * dogs_originally  # Given that the original number of dogs was half the number of cats
    result = cats_originally
    return result

print(solution())