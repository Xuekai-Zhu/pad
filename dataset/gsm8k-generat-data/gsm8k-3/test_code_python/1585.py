def solution():
    """Olly wants to get shoes to protect his pets’ paws. He owns 3 dogs, 2 cats, and a ferret. How many shoes does he need?"""
    # Define the number of shoes needed for each type of pet
    DOG_SHOES = 4
    CAT_SHOES = 4
    FERRET_SHOES = 2

    # Define the number of each type of pet
    num_dogs = 3
    num_cats = 2
    num_ferrets = 1

    # Calculate the total number of shoes needed
    total_shoes = (num_dogs * DOG_SHOES) + (num_cats * CAT_SHOES) + (num_ferrets * FERRET_SHOES)

    # Display the total number of shoes needed
    result = total_shoes
    return result

print(solution())