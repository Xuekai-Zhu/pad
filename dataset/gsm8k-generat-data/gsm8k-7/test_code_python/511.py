def solution():
    carrots = 15
    zucchini = 13
    broccoli = 8

    # Calculate the total mass of the vegetables
    total_veg_mass = carrots + zucchini + broccoli

    # Calculate the mass of vegetables sold (half of total)
    sold_veg_mass = total_veg_mass / 2
    result = sold_veg_mass
    return result

print(solution())