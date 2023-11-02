def solution():
    petals_per_rose = 8
    roses_per_bush = 12
    petals_per_ounce = 320

    # Calculate the number of petals per bottle of perfume
    petals_per_bottle = petals_per_ounce * 12

    # Calculate the number of roses needed per bottle of perfume
    roses_per_bottle = petals_per_bottle / petals_per_rose

    # Calculate the total number of roses needed for 20 bottles of perfume
    total_roses = roses_per_bottle * 20

    # Calculate the number of bushes needed
    bushes_needed = total_roses / roses_per_bush
    result = bushes_needed
    return result

print(solution())