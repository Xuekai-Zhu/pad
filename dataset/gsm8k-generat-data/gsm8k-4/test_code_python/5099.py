def solution():
    """Yesterday, the newly opened animal shelter received their first 60 animals. They got 20 more cats than dogs. How many cats did they take in?"""
    # Define the total number of animals
    total_animals = 60

    # Calculate the number of dogs and cats
    dogs = (total_animals - 20) / 2
    cats = dogs + 20

    # return the result
    result = cats
    return result

print(solution())