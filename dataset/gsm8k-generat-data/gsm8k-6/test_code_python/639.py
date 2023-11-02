def solution():
    # Calculate the total number of dogs in the community
    dogs = 15*2 + 20*1  # 15 families own 2 dogs each, 20 families own 1 dog each

    # Calculate the total number of cats in the community
    cats = (50 - 15 - 20)*2  # remaining families own 2 cats each

    # Calculate the total number of dogs and cats in the community
    total_animals = dogs + cats
    result = (dogs, cats, total_animals)
    return result

print(solution())