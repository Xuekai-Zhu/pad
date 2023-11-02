def solution():
    # Define the number of pets of each type
    num_dogs = 3
    num_cats = 2
    num_ferrets = 1

    # Calculate the total number of shoes needed (4 per dog, 4 per cat, 2 per ferret)
    total_shoes = (4 * num_dogs) + (4 * num_cats) + (2 * num_ferrets)
    result = total_shoes
    return result

print(solution())