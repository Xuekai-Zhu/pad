def solution():
    """Cassie is trimming her pet's nails. She has four dogs and eight parrots. Each dog has four nails on each foot, and each parrot has three claws on each leg, except for one parrot who has an extra toe. How many nails does Cassie need to cut?"""
    dog_nails = 4 * 4 * 4 # 4 dogs, 4 nails each foot, 4 feet
    parrot_nails = 8 * (3 * 2 + 4) # 8 parrots, 3 claws each leg (except one with 4 legs), 2 legs per parrot + extra toe
    total_nails = dog_nails + parrot_nails
    result = total_nails
    return result

print(solution())