def solution():
    """Cassie is trimming her pet's nails. She has four dogs and eight parrots. Each dog has four nails on each foot, and each parrot has three claws on each leg, except for one parrot who has an extra toe. How many nails does Cassie need to cut?"""
    # Define the number of dogs and parrots
    num_dogs = 4
    num_parrots = 8

    # Calculate the total number of dog nails
    dog_nails = num_dogs * 4 * 4

    # Calculate the total number of parrot claws
    parrot_claws = (num_parrots * 3 * 2) - 1

    # Calculate the total number of nails to cut
    total_nails = dog_nails + parrot_claws

    # Return the result
    result = total_nails
    return result

print(solution())