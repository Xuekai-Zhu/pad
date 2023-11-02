def solution():
    # Calculate the number of cats currently in Jeff's shelter
    number_of_cats = 20 + 2 + 1 - (3 * 2)  # Jeff found 2 kittens on Monday and 1 cat with an injury on Tuesday, but 3 people adopted 2 cats each on Wednesday
    result = number_of_cats
    return result

print(solution())