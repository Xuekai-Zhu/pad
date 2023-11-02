def solution():
    """Cassie is trimming her pet's nails. She has four dogs and eight parrots. Each dog has four nails on each foot, and each parrot has three claws on each leg, except for one parrot who has an extra toe. How many nails does Cassie need to cut?"""
    num_dogs = 4
    num_parrots = 8
    nails_per_dog = 4 * 4  # 4 nails on each of 4 feet
    nails_per_parrot = (3 * 2) + 4  # 3 claws on each of 2 legs, 1 extra toe on one parrot
    total_nails = (num_dogs * nails_per_dog) + (num_parrots * nails_per_parrot)
    result = total_nails
    return result

print(solution())