def solution():
    """Cassie is trimming her pet's nails. She has four dogs and eight parrots. Each dog has four nails on each foot, and each parrot has three claws on each leg, except for one parrot who has an extra toe. How many nails does Cassie need to cut?"""
    # Define the number of dogs and parrots
    num_dogs = 4
    num_parrots = 8

    # Define the number of nails on each dog's foot
    dog_nails = 4

    # Define the number of claws on each parrot's leg
    parrot_claws = 3

    # Calculate the total number of dog nails
    dog_nails_total = num_dogs * 4 * dog_nails

    # Calculate the total number of parrot claws, accounting for the extra toe
    parrot_claws_total = (num_parrots - 1) * 2 * 3 + 4

    # Calculate the total number of nails to be cut
    total_nails = dog_nails_total + parrot_claws_total

    # Display the total number of nails
    result = total_nails
    return result

print(solution())