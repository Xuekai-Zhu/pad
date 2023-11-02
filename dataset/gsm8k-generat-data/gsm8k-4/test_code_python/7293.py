def solution():
    """Brenda is a vet who needs to spay some cats and twice as many dogs. If she needs to spay 21 animals total today, how many cats does she need to spay?"""
    # Define the number of cats as x
    # Define the number of dogs as 2x (twice as many dogs as cats)
    x = None

    total_animals = 21

    # number of cats spayed
    cat_num = x 

    # number of dogs spayed
    dog_num =  2*x

    # total number of animals spayed
    total_num = cat_num + dog_num

    # Use the total number of animals to solve for x
    x = (total_animals / 3)

    # Round the result to the nearest integer
    result = round(x)
    return result

print(solution())