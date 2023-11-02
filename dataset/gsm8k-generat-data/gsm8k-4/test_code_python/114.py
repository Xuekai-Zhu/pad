def solution():
    """Ed has 2 dogs, 3 cats and twice as many fish as cats and dogs combined. How many pets does Ed have in total?"""
    # Define the number of dogs, cats, and fish
    dogs = 2
    cats = 3
    fish = (dogs + cats) * 2

    # Calculate the total number of pets
    total_pets = dogs + cats + fish

    # return the result
    result = total_pets
    return result

print(solution())