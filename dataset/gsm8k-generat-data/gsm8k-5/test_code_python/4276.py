def solution():
    petals_per_ounce = 320  # 320 rose petals make an ounce of perfume
    petals_per_rose = 8  # Each rose produces 8 petals
    roses_per_bush = 12  # There are 12 roses per bush
    ounces_per_bottle = 12  # Each bottle of perfume contains 12 ounces
    bottles = 20  # Fern wants to make 20 bottles of perfume

    # Calculate the total number of petals needed for 20 bottles of 12 ounces each
    total_petals = petals_per_ounce * ounces_per_bottle * bottles

    # Calculate the total number of roses needed, and round up to the nearest whole number
    total_roses = total_petals / petals_per_rose
    bushes = math.ceil(total_roses / roses_per_bush)
    result = bushes
    return result

print(solution())