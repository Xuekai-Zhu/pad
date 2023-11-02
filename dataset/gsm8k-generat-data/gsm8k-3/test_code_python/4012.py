def solution():
    """Michael has 2 cats and 3 dogs. He needs to pay a friend to watch them, who charges $13 a night per animal. How much does Michael have to pay?"""
    # Define the number of cats and dogs Michael has
    num_cats = 2
    num_dogs = 3

    # Define the cost per night per animal
    cost_per_animal = 13

    # Calculate the total cost for all animals for one night
    total_cost = (num_cats + num_dogs) * cost_per_animal

    # Display the total cost
    result = total_cost
    return result

print(solution())