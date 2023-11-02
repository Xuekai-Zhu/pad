def solution():
    """A fruit and vegetable merchant installed 15 kg of carrots, 13 kg of zucchini and 8 kg of broccoli. He sold only half of them. What mass of vegetables did he sell?"""
    # Define the initial amounts of carrots, zucchini, and broccoli
    carrots = 15
    zucchini = 13
    broccoli = 8

    # Calculate the total mass of vegetables
    total_veggies = carrots + zucchini + broccoli

    # Calculate the mass of vegetables sold
    veggies_sold = total_veggies / 2

    # Return the mass of vegetables sold
    result = veggies_sold
    return result

print(solution())